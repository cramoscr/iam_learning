# 25_try_catch.py 
# ------------
# Updated: cramos 02/jan/2022
#
# This sample shows how to handle errors in Python

basura
asdfasdf
asdf
asdf
asdf
asdf
12312
12
1
31
3asd1f
a3d1f
as1df
3a1sdf
a1sdf
a31dsf

while True:
    a = input('\n Enter a number value ["q" for exit]: ')

    if (a in ['q', 'Q']):
        break

    try:
        b = float(a) * 3.5
        print(f'\t This is the value of "b": {b}')
    except Exception:
        print(f'\t Error: variable "a" is not a number')

