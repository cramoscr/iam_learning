# tuples_lab.py
# Based on Python Crash Course book (page 65)
# Updated: cramos 29/may/2022

# Notes:
#  + Tuples are INMUTABLE lists....
#  + Tuple of single element required the trailing coma.  Example: size=(3,)

# Example 1
print ("\n 1___ Defining TUPLES ___")

my_figures = ('circle', 'square', 'rectangle')
for figure in my_figures:
	print (f"{figure.title()}, using title format")
	break

print(my_figures[0])

# Example 2
print ("\n 2___ Tuple with single element ___")
my_tuple = ('alone')
print(my_tuple)

# Example 3
print ("\n 3___ Raising exception because of Tuple change ___")
try:
	my_tuple[0] = 'together'
except Exception as e:
	print(e)
