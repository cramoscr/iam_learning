# 18_functions_nested.py
# -------------------
# Updated: cramos 10/oct/2022

# Based on Angela Yu: 100DaysOfCode

# Notes:
#    La verdad, no entendí bien esto... :( 
#    Tendré que repasar !!!

# Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    print(f'Calling nested_function...')
    nested_function()

print(f'Test 1. Calling outer_function....\n')
outer_function()

## Functions can be returned from other functions
def outer_function2():
    print("I'm outer (2)")

    def nested_function():
        print("I'm inner (2)")

    return nested_function


print(f'Test 2. inner_function variable gets the result of outer_function2...\n')
inner_function = outer_function2()

print(f'Test 3. This is the content of inner_function: {inner_function} ...\n')

#inner_function

print(f'...end line...')
