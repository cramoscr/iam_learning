# strings_lab1.py
# Based on Python Crash Course book
# Updated: cramos 13/may/2022

# Example 1
print ("\r\n")
print (" ___ Example1 ___")

name = "ada lovelace"
print(name.title(), '<--- title')
print(name.upper(), '<--- upper')
print(name.lower(), '<--- lower')

# Example 2 : Using funtion "f"ormat string ("f" introduced on Python 3.6)
print ("\r\n")
print (" ___ Example2: Using 'f' strings ___")
first_name = "ada"
last_name = "lovelace"
fullname = f"{first_name} {last_name}"
print(fullname)
message = f"Hello, {fullname.title()}!"
print(message)

print(f"\nAnother case: {fullname}")

# Example 3 : Using funtion "format" (python 3.5 or below) string
print ("\r\n")
print (" ___ Example3: Using 'format()' strings ___")
first_name = "ada"
last_name = "lovelace"
fullname = "{} {}".format(first_name, last_name)

print(fullname)

# Example 4 : Inserting tabs and whitspaces
print ("\r\n")
print (" ___ Example4: Inserting tabs and newline ___")
print(first_name, '\t', last_name, '<---- Tab')
print(first_name, '\n', last_name, '<---- newline')
