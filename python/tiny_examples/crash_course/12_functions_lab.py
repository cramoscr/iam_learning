# functions_lab.py
# Based on Python Crash Course book (page 133)
# Updated: cramos 04/jun/2022

# Best practices
#    + No more than two levels should be used when nesting structures
#    + It is recomended to keep the same inner structre inside the dict
#     

# Example 1
print ("\n 1___ Basic function ___")

def say_hello():
	''' Simply prints a static greeting message'''
	print('Hello there!')

say_hello()

# Example 2
print ("\n 2___ Positional arguments ___")

def describe_pet(pet_type, pet_name):
	''' Prints info about a pet based on arguments received'''
	print('I have a', pet_type, ' whose name is', pet_name)

describe_pet('dog','canelo')
describe_pet('fish','agatha')

# Example 3
print ("\n 3___ Keyword arguments ___")

def describe_pet(pet_type, pet_name):
	''' Prints info about a pet based on arguments received'''
	print('I have a', pet_type, ' whose name is', pet_name)

describe_pet(pet_name='blacky', pet_type='cat')
describe_pet(pet_type='rabbit', pet_name='whitey')

# Example 4
print ("\n 4___ Default valued arguments ___")

def describe_pet(pet_name, pet_type='dog'):
	''' Default valued argument should be possitionated on the right '''
	print('I have a', pet_type, ' whose name is', pet_name)

describe_pet(pet_name='smothie', pet_type='rabbit')
describe_pet(pet_name='pinky')

# Example 5
print ("\n 5___ Using and optional argument ___")

def describe_pet(pet_name, pet_type=''):
	''' Default valued argument should be possitionated on the right '''
	v_pet_type = pet_type
	if not v_pet_type:
		v_pet_type = 'pet'

	print('I have a', v_pet_type, ' whose name is', pet_name)

describe_pet(pet_name='smothie', pet_type='rabbit')
describe_pet(pet_name='clifford')

# Example 6
print ("\n 6___ Returning a single value ___")

def get_square(value):
	''' Returns the square value of the received argument '''
	return value * value

val = 3
print('Square value of', val, 'is:', get_square(val))

# Example 7
print ("\n 7___ Returning a Dictionary ___")

def get_person(first_name, last_name, age=None):
	''' Returns a dict structure '''
	person = {'first': first_name, 'last_name': last_name}
	if age:
		person['age'] = age
	return person

musician = get_person('jimmy', 'hendrix', age=27)
print('musician:', musician)

musician = get_person('janis', 'joplin')
print('musician:', musician)

# Example 8
print ("\n 8___ Passing a copy of a list ___")

def pop_and_print (pList):
	while pList:
		val = pList.pop()
		print('Value:', val)

my_list = ['bike', 'car', 'truck', 'plane']

pop_and_print(my_list[:])
print(my_list, '<------ my_list (rslt 1)')

# This way, list content is modified
pop_and_print(my_list)

print(my_list, '<------ my_list (rslt 2)')


# Example 9
print ("\n 9___ Passing an arbitrary quantity of arguments ___")

def make_pizza (size, *toppings):
	''' Summarize the pizza toppings'''
	print(f"\nMaking a {size}-inch pizza with this toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Example 10
print ("\n 10___ Passing an arbitrary Keyword Arguments ___")

def build_profile (first, last, **user_info):	
	''' Builds a dictionary containing everything we know about a user '''
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', 
	                          field='physics', origin='germany')

print(user_profile)
