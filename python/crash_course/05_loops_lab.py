# loops_lab.py
# Based on Python Crash Course book (page 53)
# Updated: cramos 29/may/2022

# Differences between "for" and "while" 
#    - for keeps going until no more data
#    - while keeps going until the "while condition" is meet or find a "break"

# Example 1
print ("\n 1___ For Loop ___")

motorcycles = ['vespa', 'yamaha', 'suzuki', 'triumph', 'honda', 'kawasaki']
for motorcycle in motorcycles:
	print (motorcycle)
	print (f"{motorcycle.title()}, in title format")

# Example 2
print ("\n 2___ Range(0, 5) function ___")

for val in range(0, 5):
	print (val)

# Example 3
print ("\n 3___ Using list(range(1,5)) ___")

numbers = list(range(1,5))
for number in numbers:
	print (number)

# Example 4
print ("\n 4___ Generating EVEN numbers ___")

numbers = list(range(1,11,2))
for number in numbers:
	print (number)

# Example 5
print ("\n 5___ Generating SQUARE numbers ___")

squares = []
for number in range(1,11):
	squares.append(number**2)

print(squares)

# Example 6
print ("\n 6___ While loop ___")

num = 1
while num <= 5:
	print('num:', num)
	num += 1

num = 100
while True:
	print('num:', num)
	num += 1
	if num > 105:
		break

# Example 7
print ("\n 7___ While + lists ___")

unconfirmed_users = ['alice', 'bryan', 'mery']
confirmed_users =[]

print('Unconfirmed (before):', unconfirmed_users)
print('Confirmed (before):', confirmed_users)

while unconfirmed_users:
	usr = unconfirmed_users.pop()
	confirmed_users.append(usr)

print('Unconfirmed (after):', unconfirmed_users)
print('Confirmed (after):', confirmed_users)

# Example 8
print ("\n 8___ Removing instances of 'dog' from a list ___")

pets = ['bird', 'cat', 'goldfish', 'dog', 'horse', 'goldfish', 'dog', 'fish', 'rabbit']
print('Pets:', pets)

while 'goldfish' in pets:
	pets.remove('goldfish')

print('Pets:', pets)
