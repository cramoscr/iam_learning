# rock_paper_scicssors.py
# --------------------
# Updated: cramos 06/ago/2022
# Based on TheLondonApp's "100Days of Python" course

import random

# Section 1 - Lovely symbols

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Section 2 - Processing

symbols = [rock, paper, scissors]

my_opt = int(input('Enter your choice: 0-rock, 1-paper, 2-scissors : '))

print(f'Your choice: {my_opt} \n {symbols[my_opt]}')

comp_opt =  random.randint(0,2)

print(f'Computer choice: {comp_opt} \n {symbols[comp_opt]}')

if    my_opt == 0 and comp_opt == 0:
	print(f'Empate en Rock !')
elif my_opt == 0 and comp_opt == 1:
	print(f'You loose :(')
elif my_opt == 0 and comp_opt == 2:
	print(f'You win :)')
elif my_opt == 1 and comp_opt == 0:
	print(f'You win :)')
elif my_opt == 1 and comp_opt == 1:
	print(f'Empate en Paper !')
elif my_opt == 1 and comp_opt == 2:
	print(f'You loose :(')
elif my_opt == 2 and comp_opt == 0:
	print(f'You loose :(')
elif my_opt == 2 and comp_opt == 1:
	print(f'You win :)')
elif my_opt == 2 and comp_opt == 2:
	print(f'You Empate en Scissors !')
