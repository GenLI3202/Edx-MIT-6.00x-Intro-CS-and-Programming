# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # First, implement the function isWordGuessed that takes in 
    # two parameters - a string, secretWord, and a list of letters,
    # lettersGuessed. This function returns a boolean - True if 
    # secretWord has been guessed (ie, all the letters of secretWord
    # are in lettersGuessed) and False otherwise.

    
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            secretWord = secretWord.replace(letter,'_ ',1)
    if '_' in secretWord:
        return False
    else:
        return True
    
# print(isWordGuessed('apple', ['e', 'i', 'p', 'p', 'l', 'a']))
# print(isWordGuessed('apple', ['e', 'i', 'k', 'p', 'l', 'a']))
    
    
    
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            secretWord = secretWord.replace(letter,'_ ', 1)
    return secretWord

# print(getGuessedWord('apple', ['e', 'i', 'p', 'p', 'j', 'a']))
# print(getGuessedWord('aapple', ['e', 'i', 'k', 'p', 'r', 's']))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    # import string
    lettersAvai = string.ascii_lowercase
    for letter in lettersGuessed:
        lettersAvai = lettersAvai.replace(letter, '', 1)
    return lettersAvai



def letsGuess(secretWord, lettersGuessed, yourChances):
    '''
    The Guess-Word-Game starts
    Parameters
    ----------
    secretWord : string
        the word to be guessed
    lettersGuessed : list
        the guessed letters be given by the user
    yourChances : int
        the chances left to the user

    Returns
    -------
    if chances != 0 and word is not guessed
        return "a new guess with updated Guessed letters"
    if no chance left
        return false
    if word is guessed
        return True
    '''
    print("You have "+ str(yourChances) + " guesses left.")
    availLetters = getAvailableLetters(lettersGuessed)
    print("Available letters: " + availLetters)
    yourGuess = input("Please guess a letter: ")
    GuessInLower = yourGuess.lower()
    if GuessInLower in lettersGuessed:
        print("Oops! You've already guessed that letter: " + 
              getGuessedWord(secretWord, lettersGuessed))
        print("-------------")
        return letsGuess(secretWord, lettersGuessed, yourChances)
    elif GuessInLower not in lettersGuessed:
        lettersGuessed.append(GuessInLower)     
            # type(lettersGuessed): list        
    guessedNow = getGuessedWord(secretWord, lettersGuessed)
    if GuessInLower in secretWord:
        print("Goodguess: " + guessedNow)
        print("-------------")        
        if secretWord == guessedNow:
            return True 
        return letsGuess(secretWord, lettersGuessed, yourChances)
    elif GuessInLower not in secretWord:
        print("Oops! That letter is not in my word: " + guessedNow)
        print("-------------")
        yourChances -= 1
        if yourChances == 0:
            return False
        else:
            return letsGuess(secretWord, lettersGuessed, yourChances)






def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''        
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")    
    lettersGuessed = []
    yourChances = len(secretWord) + 8
    Result = letsGuess(secretWord, lettersGuessed, yourChances)
    if Result == True:
        return print("Congratulations, you won!")
    else:
        return print("Sorry, you ran out of guesses. The word was " + secretWord)
    
    
         
    
        
    
    
# Hints: 
# =============================================================================
# a. four important pieces of information you may wish to store:
    # 1. secretWord: The word to guess.
    # 2. lettersGuessed: The letters that have been guessed so far.
    # 3. mistakesMade: The number of incorrect guesses made so far.
    # 4. availableLetters: The letters that may still be guessed. Every 
                # time a player guesses a letter, the guessed letter must be removed 
                # from availableLetters (and if they guess a letter that is not in 
                # availableLetters, you should print a message telling them they've 
                # already guessed that - so try again!).    
# b. Consider using lower() to convert user input to lower case. 
#    For example:
        # guess = 'A'
        # guessInLowerCase = guess.lower()

# =============================================================================




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
