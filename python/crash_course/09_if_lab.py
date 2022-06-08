# if_lab.py
# Based on Python Crash Course book (page 77)
# Updated: cramos 04/jun/2022

# Example 1
print ("\n 1___ If statements ___")

val = input("Enter a any value (number o string):")
if val.isdigit() == True:
	x = int(val)
	if x > 10:
		print('x is bigger than 10')

	if x >= 10:
		print('x is bigger or equal than 10')

	if x <= 10:
		print('x is lower or equal than 10')

	if x <= 10 or x > 100:
		print('x is lower than 11 or bigger than 100')

if type(val) is str:
	print('val is string')
	if val == 'abc':
		print('Val is abc')

# Example 2
print ("\n 2___ Checking lists ___")
brands = ['ibm', 'samsung', 'nokia']
brand = 'iphone'
if brand not in brands:
	print(brand, ' is not in ', brands)

# Example 3
print ("\n 3___ If else chaining ___")
x = input('Enter a number value:')
x = int(x)
if x > 20:
	print('x is bigger than 20')
elif x < 10:
	print('x is lower than 10')
else:
	print('other case')





