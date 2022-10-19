# operators_lab.py
# Based on Python Crash Course book (page 117)
# Updated: cramos 13/may/2022

# Example 1
print ("\n")
print (" ___ 1. Modulo operator ___")

rslt = 5 % 3
print(rslt, '<----- 5 % 3 ')

rslt = 6 % 3
print(rslt, '<----- 6 % 3 ')

rslt = 7 % 3
print(rslt, '<----- 7 % 3 ')

# Example 2
print ("\n")
print (" ___ 2. Even or Odd ___")

num = input('Enter a number:')

if int(num) % 2 == 0:
	print('The number is Even.')
else:
	print('The number is Odd.')

