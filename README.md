##Python Hangman

A command line Hangman game written in Python.

####Run Options:
- `hangman.py` to play the game with the provided **dictionary.txt** word list.
- `hangman.py --input` to play the game with a word randomly chosen from a text file of your choice.

####Instructions:
The user is asked for a word length and a number of guesses before beginning, but keep in mind that: 
- a word length of 0 means that any word in the list may be chosen.
- a negative number of guesses will be negated (e.g. -5 becomes 5).
- a non-integer number of guesses will be truncated (e.g. 3.2 becomes 3).
