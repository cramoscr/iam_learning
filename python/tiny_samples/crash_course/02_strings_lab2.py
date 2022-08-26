# strings_lab2.py
# Based on Python Crash Course book (page 25)
# Updated: cramos 13/may/2022

# Example 1
print ("\n")
print (" ___ Personal Message ___")

name = "Eric"
print('Hello',name,'would you like to learn some Python today?')

# Example 2
print ("\n")
print (" ___ Name Cases ___")

name = "Eric"
print(name.lower(),'<----- lowercase')
print(name.upper(),'<----- uppercase')
print(name.title(),'<----- title')

# Example 3
print ("\n")
print (" ___ lstrip() ___")

name = "  MrBig  "
print(name, '<----- original')
print(name.lstrip(), '<----- left strip')

# Example 4
print ("\n")
print (" ___ rstrip() ___")

name = "  MrBig  "
print(name, '<----- original')
print(name.rstrip(), '<----- right strip')

# Example 5
print ("\n")
print (" ___ strip() ___")

name = "  MrBig  "
print(name, '<----- original')
print(name.strip(), '<----- strip')


