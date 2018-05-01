"""
In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
e.g.
Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.
"""
# vars
low = 0
high = 100
guess = (high + low) / 2
epsilon = 0.01
game_on = True

# helpers
def check_answer():
    global game_on, high, low, guess
    print('Is your secret number ',str(round(guess)), '?',sep = '')
    answer = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
    if answer == 'c':
        print('Game over. Your secret number was: ', guess)
        game_on = False
    elif answer == 'h':
        high= guess
    elif answer == 'l':
        low = guess
    else:
        print('Sorry, I did not understand your input.')
        check_answer()
    guess = int((high +  low) / 2)
    return guess

# get user's number

print('Please think of a number between 0 and 100!\n')

while game_on:
    check_answer()

