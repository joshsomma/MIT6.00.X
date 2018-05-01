# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random, string

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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guess = ''
    for l in secretWord:
        if l in lettersGuessed:
            guess += l
    return guess == secretWord

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess = ''
    for l in secretWord:
        if l in lettersGuessed:
            guess += l
        else:
            guess += ' _ '
    return guess

def getAvailableLetters(lettersGuessed):
    letters = string.ascii_lowercase
    temp_string = ''
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in letters:
            temp_string = letters.replace(lettersGuessed[i],'')
            letters = temp_string
    return letters




# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

# helper code for EdX answer (to include)

def takeTurn(turn_count,lettersGuessed):
    print('You have ', turn_count, ( 'guesses left.'))
    print('Available letters: ', getAvailableLetters(lettersGuessed))
    return input('Please guess a letter: ')

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
    
    # set up game vars
    turn_count = 8
    lettersGuessed = []
    turn_guess = ''

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ', str(len(secretWord)), 'letters long.')
    print('-----------')
    while turn_count > 0:
      print('You have ', turn_count, ( 'guesses left.'))
      print('Available letters: ', getAvailableLetters(lettersGuessed))
      turn_guess = input('Please guess a letter: ')
      while turn_guess in lettersGuessed:
        print('Oops! You\'ve already guessed that letter: ', getGuessedWord(secretWord, lettersGuessed))
        print('-----------')
        print('You have ', turn_count, ( 'guesses left.'))
        print('Available letters: ', getAvailableLetters(lettersGuessed))
        turn_guess = input('Please guess a letter: ')
      lettersGuessed.append(turn_guess)
      if turn_guess in secretWord:
          print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
          print('-----------')
          turn_count += 1
          if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            won = True
            break
      else:
          print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
          print('-----------')
          won = False
          
      turn_count -= 1
    if not won:
        print('Sorry, you ran out of guesses. The word was ', secretWord)

#secretWord = chooseWord(wordlist).lower()
secretWord = 'else'
hangman(secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
