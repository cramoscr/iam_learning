# functions_adv_lab.py
# Based on Python Crash Course book (page 153)
# Updated: cramos 04/jun/2022

# Notes:
#   This lab is correlated with a file called module_pizza.py

# Example 1
print ("\n 1___ Importing full module ___")

import module_pizza as my_mod

my_mod.make_pizza(8, 'pepperoni')
my_mod.print_price(8)

my_mod.make_pizza(10, 'mushrooms', 'green peppers', 'extra cheese')
my_mod.print_price(10)

# Example 2
print ("\n 2___ Importing specific function ___")

from module_pizza import make_pizza as my_func

my_func(4, 'ham')
my_func(6, 'pineaple', 'meal', 'onion')
