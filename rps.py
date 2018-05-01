#!/bin/python3
# libs
from random import randint

# global vars
game_on = True

# helper functions
def game_turn():
  # get player choice
  player = input('rock (r), paper (p) or scissors (s)? ')
  
  # print out choice
  print(player, 'vs', end=' ')
  
  # choose random number between 1-3 for computer choice
  chosen = randint(1,3)
  
  #print(chosen)
  
  if chosen == 1:
    computer = 'r'
  elif chosen == 2:
    computer = 'p'
  else:
    computer = 's'
    
  print(computer)
  
  if player == computer:
    print('DRAW!')
  # eval for player choosing rock
  elif player == 'r' and computer =='s':
    print('Player wins!')
  elif player == 'r' and computer == 'p':
    print('Computer wins!')
  # eval for player choosing paper
  elif player == 'p' and computer == 'r':
    print('Player wins!')
  elif player == 'p' and computer == 's':
    print('Computer wins!')
  # eval for player choosing scissors
  elif player == 's' and computer == 'p':
    print('Player wins!')
  elif player == 's' and computer == 'r':
    print('Computer wins!')

  start_over()

def start_over():
    global game_on

    again = input('Do you want to play again? y/n ')
    if again == 'y':
        game_on = True
        game_turn()
    elif again == 'n':
        print('Thanks for playing!')
        game_on = False
    else:
        print('Thanks for playing!')
        game_on = False

# welcome message    
print('Welcome to Rock, Paper, Scissors!')

while game_on == True:
    game_turn()
    

