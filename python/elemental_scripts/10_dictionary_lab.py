# dictionary_lab.py
# Based on Python Crash Course book (page 93)
# Updated: cramos 04/jun/2022

# Notes:
#   + Dictionaries retain the order in which key were defined

# Example 1
print ("\n 1___ Basic dictionary ___")

allien = {'color':'green', 'points':5}
print(allien, '<----- full dictionary')
print('color:', allien['color'])
print('points:', allien['points'])

# Example 2
print ("\n 2___ Starting with empty dict ___")

allien = {}
allien['color'] = 'blue'
allien['points'] = '13'

print(allien, '<----- full dictionary')
print(len(allien), '<----- length')

# Example 3
print ("\n 3___ Adding items ___")

allien = {'color':'green', 'points':5}
print(allien, '<----- full dictionary')
allien['x_position'] = 0
allien['y_position'] = 25
print(allien, '<----- keys added')
print(len(allien), '<----- length')

# Example 4
print ("\n 4___ Using del dict_x['key_x'] ___")

allien = {'color':'green', 'points':5}
print(allien, '<----- full dictionary')
del allien['points']
print(allien, '<----- after removal')

# Example 5
print ("\n 5___ Using get() ___")

allien = {'color':'green', 'speed':'low', 'points':8}
print(allien, '<----- full dictionary')
rslt = allien.get('speed', 'Speed not found...')
print(rslt, '<----- Speed rslt')

rslt = allien.get('size', 'Size not found...')
print(rslt, '<----- Size rslt')

rslt = allien.get('height')
print(rslt, '<----- Height rslt')

# Example 6
print ("\n 6___ Looping through all [key,val] ___")

allien = {'color':'green', 'speed':'low', 'points':8}
for k, v in allien.items():
	print('Key: ', k, ' Value: ', v)

# Example 7
print ("\n 7___ Looping through all keys ___")

allien = {'color':'green', 'speed':'low', 'points':8}
for k in allien.keys():
	print('Key: ', k)

# Example 8
print ("\n 8___ Looping through all values ___")

allien = {'color':'green', 'speed':'low', 'points':8}
for v in allien.values():
	print('Value: ', v)

# Example 9
print ("\n 9___ Using sorted(dict.keys()) ___")

allien = {'color':'green', 'speed':'low', 'points':8}
print(allien, '<----- unsorted full dictionary')
print(sorted(allien), '<----- ordered full dictionary')
for k in sorted(allien.keys()):
	print('Key: ', k)

# Example 10
print ("\n 10___ Looking for specific name ___")

allien = {'color':'green', 'speed':'low', 'points':8}
if 'size' not in allien.keys():
	print('Size key is not in alliens dict')

