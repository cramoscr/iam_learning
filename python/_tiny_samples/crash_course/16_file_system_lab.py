# 16_file_system_lab.py
# Based on Python Crash Course book (page 177)
# Updated: cramos 11/jun/2022

# Key notes:
#   Python has no limits about the size of the files to work with
#   (limited on by the RAM of the machine)

# Example 1
print ("\n 1___ Basic: open local file ___\n")

fh = open("text_file_sample.txt")
myDict = dict()
lst = list()

for line in fh:
	print(line)

# Trick: In this moment the buffer of the fh is empty
print(fh.readlines())     # print full content of the file


# Example 2
print ("\n 2___ Basic: reading fullcontent ___\n")

fh = open("text_file_sample.txt")
myDict = dict()
lst = list()

print(fh.readlines())     # print full content of the file


# Example 3
print ("\n 3___ Basic: open file using 'with' ___\n")

my_filename = "text_file_sample.txt"
try:
	with open(my_filename) as my_file_object:
		my_content = my_file_object.read()
		print('File content:\n', my_content)
except FileNotFoundError:
	print(f"Sorry, the file {my_filename} does not exist")

# Example 3
print ("\n 3___ Basic: using longer file path source ___\n")

with open('c:/Temp/Coursera.txt') as my_file_object:
	my_content = my_file_object.read()

print('File content:\n', my_content)


# Example 4
print ("\n 4___ Basic: readling lines ___\n")

with open('text_file_sample.txt') as my_file_object:
	for my_line in my_file_object:
		print(my_line.rstrip())


# Example 5
print ("\n 5___ Using readlines() ___\n")

with open('text_file_sample.txt') as my_file_object:
	my_lines = my_file_object.readlines()

for line in my_lines:
	print(line)


# Example 6
print ("\n 6___ Writting to a file ___\n")

with open('text_file_sample.out', 'w') as my_file_object:
	my_file_object.write("This is the first line.\n")
	my_file_object.write("This is the second line.\n")
	my_file_object.write("This is the third line.\n")

with open('text_file_sample.out') as my_file_object:
	print(my_file_object.readlines())

