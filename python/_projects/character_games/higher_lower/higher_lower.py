# higher_lower.py
# ------------
# Updated: cramos 17_oct_2022

# Based on TheLondonApp Brewery [ 100DaysOfCode ]

# Section 1 - Imports

import random
import os

from higher_lower_img import logo_img, vs_img, win_img, loose_img

from higher_lower_data import data


# Section 2 - Functions

def produceFact(pLabel):
	""" Prints a fact from data dictionary based on random number """
	vIndex = random.randint(0, len(data)-1)
	vDictionary = data[vIndex]
	print(f" {pLabel.upper()}. {vDictionary['name']}  [ {vDictionary['country']} - {vDictionary['description']} ] >> {vDictionary['follower_count']} ")
	return int(vDictionary['follower_count'])

def chechAnswer(pChoice, pFollowersA, pFollowersB):
	""" Checks if the user guesses the correct answer """
	if (pFollowersA > pFollowersB):
		return pChoice == "a"
	else:
		return pChoice == "b"

	return False


# Section 3 - Main loop

vScore = 0
vDict = {}

while True:

	os.system('cls')

	print(logo_img)

	# Choose the first data (called A)
	vFollowersA = produceFact('A')

	print(vs_img)

	# Choose the second data (called B)
	vFollowersB = produceFact('B')

	while True:
		vChoice = input('\n Which one have more followers A or B ? (enter Q to exit): ')
		vChoice = vChoice.lower()

		if vChoice.lower() in ['a', 'b', 'q']:
			break

	# Exit when answer is "q"
	if vChoice.lower() == "q":
		break

	# Check if the user answer is right of wrong
	if chechAnswer(vChoice, vFollowersA, vFollowersB):
		vScore += 1
		print(win_img)
	else:
		print(loose_img)

	print(f"You current score: [ {vScore} ]")

	input('Press ENTER to continue...')
