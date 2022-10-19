# 24_local_vs_global_scope.py
# ------------------------
# Updated: cramos 17/oct/2022

# Notes:
#    
#   It's highly recomended not modify Global variables inside a functions


# Section 1 (local scope)

# variables defined inside a function can only be referenced
# within the function

def myFunction (pValue):
	my_local = pValue * 3
	return my_local + my_global


# Section 2 (modifying a Global variable inside a function)
def myOtherFunction:
	global my_global     # If we omit this statement, the "my_global" will be a local variable
	my_global += 11111   # and will produce an execution error
	return my_global

# Section 2 (Global scope)

my_global = 10  # This variable will be accesible in any place

# This line will produce an error because my_local can only be referenced
# inside the myFunction()
if (my_local == 1):
	print(f'this must produce an error')


print(f'This is myFunction result: {myFunction(10)}')


# Section 3 (Global scope)
if (1 == 1):
	my_anotherglobal = 'cool'  # This can be referenced as Global

print (f'This is my_anotherglobal: {my_anotherglobal}')

