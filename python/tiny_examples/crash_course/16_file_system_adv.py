# 16_file_system_adv_lab.py
# Based on Python Crash Course book (page 177)
# Updated: cramos 11/jun/2022

# Example 1
print ("\n 1___ Writting output file as JSON ___\n")

import json
numbers = [1,2,3,4,5,11,23,37,127]
filename = 'numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)

with open(filename) as f:
	print(f"Output: {f.readlines()}")
