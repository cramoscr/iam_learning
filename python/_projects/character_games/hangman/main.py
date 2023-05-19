# main.py
# -------
# Updated: cramos 02/mar/2023
# Based on TheLondonApp Brewery 100DaysOfPython
# This is a character GUI based game
#   Simulates the hangman game

# Try it:
#   $ python3 main.py

import os 

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["anything", "happy", "treasure", "rock&roll", "camel", "elephant", "biggest"]
chosed_word = random.choice(word_list)
word_length = len(chosed_word)

lives = 6

#Testing code
print(f'Pssst, the solution is {chosed_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    print(f'\n Welcome to the Hangman Game \n')
    print(f'Remaining lives: {lives}')

    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosed_word[position]
        if letter == guess:
            display[position] = letter
        else:
          guessed = False
          lives -= 1
    
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if lives < 1:
        end_of_game = True
        print("You loose.")
        
        
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    os.system('clear')
    print(stages[lives])
