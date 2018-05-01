SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# print(getFrequencyDict("mississippi"))

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """

    word_score = 0 # var for the score we want to return

    # if the string is empty, return a score of zero
    if len(word) == 0:
        return 0

    # check if word equals the total number of letters in the hand; add 50 pts if yes
    if len(word) == n:
        word_score += 50

    letters_score = 0 # set a var to keep score of letters in the word

    # call getFrequencyDict to return a dict w frequency of letters
    freq = getFrequencyDict(word)

    # loop over each value in freq; multiply freq of letter *'s value of letter; total up score of all letters
    for l in freq:
        # print('Letter value: ', letter_val)
        # print('Frequency of letter: ', str(freq[l]))
        # print('Letter value *\'s frequency of letter', str(letter_val * freq[l]))
        letters_score += SCRABBLE_LETTER_VALUES[l] * freq[l]
    
    # multiply letters_score *'s len of word to get total word score
    word_score += letters_score * len(word)

    return word_score

print(getWordScore("", 7)) # result 0
print(getWordScore("it", 7)) # result 4
print(getWordScore("scored", 7)) # result 54
print(getWordScore("waybill", 7)) # result 155