# 25_try_catch.py 
# ------------
# Updated: cramos 02/jan/2022
#
# This sample shows how to handle errors in Python

while True:
    a = input('\n Enter a number value ["q" for exit]: ')

    if (a in ['q', 'Q']):
        break

    try:
        b = float(a) * 3.5
        print(f'\t This is the value of "b": {b}')
    except Exception:
        print(f'\t Error: variable "a" is not a number')

