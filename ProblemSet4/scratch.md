**Steps to solve getWordScore**

* Write down a variable to hold the score we want to return (e.g. word_score = 0)
* Write down the word we want to test
* Is the word longer than the total number of lettes in the hand?
* * Return an error message and prompt for a new word; start over
* Is the word empty?
* * 3.1 Yes: leave score at 0 and return score
* * 3.2 No: go to the next step 
* Is the lenth of the word == the total number of letters in the hand?
* * 4.1 Yes: add 50 to score; go to the next step
* * 4.2 No: go to the next step
* Write down a variable to hold the total score of the letters (e.g. letters_score = 0)
* Write down frequency of each letter in word
* Go through each letter in word
* * multiply the frequency of each letter *'s its value contained in SCRABBLE_LETTER_VALUES
* * add this value to letters_score
* Multiply letters_score * len(word); add the product to word_score
* Return word_score




**Pseudo code**

// inputs: word: string; n: int >=0

// word_score = 0

// if len(word) == 0:
//  return 0

//if len(word) == n:
//  word_score += 50

// letters_score = 0

// get frequency of each letter; store in dict (using helper function)

// loop through dict
//  for each letter:
//      look up value in SCRABBLE_LETTER_VALUES
//      letters_score += freq * value of letter

// word_score += letters_core * len(word)


//return word_score
        