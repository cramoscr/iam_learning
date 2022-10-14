# dictionary_adv_lab.py
# Based on Python Crash Course book (page 106)
# Updated: cramos 04/jun/2022

# Best practices
#    + No more than two levels should be used when nesting structures
#    + It is recomended to keep the same inner structre inside the dict
#     

# Example 1
print ("\n 1___ Dict nesting: dict inside a list ___")

alien1 = {'color':'green', 'points':3}
alien2 = {'color':'black', 'points':12}
alien3 = {'color':'blue', 'points':500}
aliens = [alien1, alien2, alien3]

print('Print aliens: \n\t', aliens)

print('Looping...')
for alien in aliens:
	print(alien)


# Example 2
print ("\n 2___ Dict nesting: bulk creation ___")

aliens = []
for x in range(10):
	alien = {'id':x, 'color':'green', 'points': x*5}
	aliens.append(alien)

print(aliens, '<----- full list')
print(len(aliens), '<----- length')

# Example 3
print ("\n 3___ Dict nesting: modifying last 3 items ___")

for alien in aliens[-3:]:
	alien['color'] = 'pink'

print(aliens, '<----- full list')
print(len(aliens), '<----- length')

# Example 4
print ("\n 4___ Dict nesting: list inside a dict ___")

pizza = {
    'id':1,
	'pasta':'gruesa',
	'toppings': ['queso', 'hongos', 'piña']
}

print('Pizza:', pizza)

pizza2 = {
    'id': 2,
	'pasta':'delgada',
	'toppings': ['chile', 'tocino']
}

pizzas = [pizza, pizza2]
print('Pizzas:', pizzas)

# Example 5
print ("\n 5___ Dict nesting: dict inside a dict ___")

users = {
	'aeinstein': {	
		'firstname': 'albert',
		'lastname': 'einstein',
		'location': 'princeton'
		},
	'mcurie': {	
		'firstname': 'mary',
		'lastname': 'curie',
		'location': 'paris'
		}
}

print('Users:', users)

print('For loop')
for username, user_info in users.items():
	print('Username:', username, ' UserInfo:', user_info)

