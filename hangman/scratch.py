
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


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

print(isWordGuessed(secretWord, lettersGuessed))

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
print(getGuessedWord(secretWord, lettersGuessed))


import string



def getAvailableLetters(lettersGuessed):
    letters = string.ascii_lowercase
    temp_string = ''
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in letters:
            temp_string = letters.replace(lettersGuessed[i],'')
            letters = temp_string
    return letters

print(getAvailableLetters(lettersGuessed))


        