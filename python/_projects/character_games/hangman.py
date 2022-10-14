# hangman.py
# -------
# Updated: cramos 09/ago/2022
# Based on TheLondonApp Brewery 100DaysOfPython

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

end_of_game = False
word_list = ["anything", "happy", "treasure", "rock&roll", "camel", "elephant", "biggest"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Testing code
#print(f'Pssst, the solution is {chossen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f'\n Welcome to the Hangman Game \n') 
    print(f'Lives: {lives}')

    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        else:
          guessed = False
      
    if not guessed:
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

    os.system('cls')
    print(stages[lives])
