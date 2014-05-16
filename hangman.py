'''
	Python Command Line Hangman

The user is asked for a word length and a number of guesses before the start
of the game.

Run Options:
- hangman.py 		Play the game with the provided Dictionary.txt word list.
- hangman.py --input 	Play the game with a word randomly chosen from a text
			file of your choice.

Note: 
- A word length of 0 means that any word in the list may be chosen.
- A negative number of guesses is made positive (so -5 becomes 5).
- A float/decimal number of guesses is truncated to an integer.
'''

import math
import random
import re
import string
import sys
import tkFileDialog

def get_textfile_name():
	filename = tkFileDialog.askopenfilename()
	while filename and not re.search(r'.+\.txt', filename):
		print "error, you must choose a text (.txt) file"
		filename = tkFileDialog.askopenfilename()
	if not filename:
		print "goodbye, exiting hangman...\n\n\n\n"
		sys.exit(1)
	return filename

def get_word_list(filename):
	with open(filename, "r") as f:
		words = f.read().split() # list of words
		wordLengths = list( set([len(word) for word in words]) )
	return (words, wordLengths)
	
def get_secret_word(words, wordLength):
	word = words[ random.randint(0, len(words)-1) ]
	while wordLength > 0 and len(word) != wordLength:
		word = words[ random.randint(0, len(words)-1) ]
	return word.lower()

def print_info(word, goodGuesses, badGuesses, missesLeft):
	print "-------------------------------------------------"
	secret = ""
	for i in range(0, len(word)):
		if word[i] in goodGuesses:
			secret += word[i] + " "
		elif word[i] == " ":
			secret += "  "
		else:
			secret += "_ "
	print "\n%s" % secret
	print "misses left: %d" % missesLeft
	print "bad guesses so far:", badGuesses
	
def ask_for_letter(message):
	letter = raw_input(message).lower()
	while not letter in string.lowercase:
		print "error, you must choose a letter"
		letter = raw_input(message).lower()
	return letter

def ask_for_int(message, unsigned=True):
	num = math.trunc( eval(raw_input(message)) )
	while not isinstance(num, int):
		print "error, you must choose an integer"
		num = math.trunc( eval(raw_input(message)) )
	if unsigned:
		num = abs(num)
	return num

def check_guess(word, missesLeft, goodGuesses, badGuesses):
	guess = ask_for_letter("\n>> guess a letter: ")
	while guess in goodGuesses or guess in badGuesses:
		print "you already guessed \"%s\"" % guess
		guess = ask_for_letter("\n>> guess a letter: ")
	
	if guess not in word:
		badGuesses.append(guess)
		missesLeft -= 1
		print "no \"%s\" in the secret word" % guess
	else:
		goodGuesses.append(guess)
	return (missesLeft, goodGuesses, badGuesses)

def play(word, missesLeft):
	badGuesses = []
	goodGuesses = []
	if re.search(r'\s', word):
		goodGuesses.append(" ")
	victory = False
	target = sorted(list(set(word)))

	while missesLeft > 0 and not victory:
		print_info(word, goodGuesses, badGuesses, missesLeft)
		(missesLeft, goodGuesses, badGuesses) = check_guess(word, missesLeft, goodGuesses, badGuesses)
		victory = ( sorted(goodGuesses) == target )
	
	end_game(word, missesLeft, victory)

def end_game(word, missesLeft, victory):
	print "-------------------------------------------------"
	if missesLeft == 0:
		print "\nyou lose :-(, the secret word was: \"%s\"" % word
	elif victory:
		print "\nsuccess! :), you found the word: \"%s\"" % word
	
	againMessage = "\nDo you want to play another game (yes or no)? "
	again = raw_input(againMessage).lower()
	while again not in ["yes", "no"]:
		again = raw_input(againMessage).lower()
	if again == "yes":
		print "\n\n"
		main()
	else:
		print "Thanks for playing!\n\n\n\n"

def main():
	if len(sys.argv) == 2 and sys.argv[1] != "--input":
		print "wrong input, enter either:\nhangman.py or hangman.py --input"
		sys.exit(1)
	else:
		if len(sys.argv) < 2:
			filename = "dictionary.txt"
		elif sys.argv[1] == "--input":
			filename = get_textfile_name()
			#del sys.argv[1]
		
		print "\nHANGMAN\n\ndictionary in use: %s\n" % filename
		
		(words, wordLengths) = get_word_list(filename)

		available = "available word lengths: " + str(wordLengths)
		msg = ">> choose a # of letters for the secret word (0 for random): "
		wordLength = ask_for_int(msg)
		while wordLength != 0 and wordLength not in wordLengths:
			print "\nthe chosen dictionary does not contain",
			print "any words of this length\n"
			wordLength = ask_for_int(available + "\n\n" + msg)
		
		missesLeft = ask_for_int("\n>> choose a # guesses: ")
		
		play(get_secret_word(words, wordLength), missesLeft)

if __name__ == "__main__":
	main()
