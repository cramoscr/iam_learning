# main.py
# -------
# Updated: cramos 02/mar/2023
# Simple character GUI based game
# 
# Try it:
#    $ python3 main.py
#

import os 

from bidder_logo import logo

offers = {}

while True:
	# Clear the screen
	os.system('cls')
	
	print(f'Welcome to Auction Simulator')
	print(logo)

	answer = input('Do you want to add an offer [y/n] ? ');

	if answer == 'n':
		break

	name = input('What is your Name: ')
	price = input('Enter the amount of your bid: ')

	offers[name] = int(price)

	winner = ''
	price = 99999999999
	for key in offers:
		if offers[key] < price:
			winner = key
			price = offers[key]


print(f'The winner of the auction is {winner} with a offer of {price} USD')

