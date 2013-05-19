Python Hangman
==============

A command line Hangman game in Python.

The user is asked for a word length and a number of guesses before the start of the game.

Run Options:
- `hangman.py` to play the game with the provided Dictionary.txt word list.
- `hangman.py --input` to play the game with a word randomly chosen from a text file of your choice.

Note: 
- A word length of 0 means that any word in the list may be chosen.
- A negative number of guesses is negated positive (e.g. -5 becomes 5).
- A float/decimal number of guesses is truncated to an integer.
