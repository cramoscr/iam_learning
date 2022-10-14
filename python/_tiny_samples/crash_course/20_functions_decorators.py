# 20_functions_decorators.py
# -----------------------
# Updated: cramos 10/oct/2022
# (based on Angela Yu: 100DaysOfCode)

import time

def delay_decorator(function):
    """ This decorator calls a sleep delay for 5 sec """

    # Before calling the function
    print(f'Sleeping for 5 seconds...\n')
    time.sleep(5)

    # Executing the function
    function()

    # After function execution
    print('The requested function was executed...\n')

# Defining and executing the say_hello() : called "syntactic sugar"
@delay_decorator
def say_hello():
    print ('Hello there...\n')

def say_bye():
    print('Good bye...\n')

# The say_hello() cannot be called "normally"
#say_hello()

# Calling the normal function
say_bye()


# Calling using decorator without syntactic suger
my_decorated = delay_decorator(say_bye)
my_decorated()

