# lists_adv_lab.py
# Based on Python Crash Course book (page 53)
# Updated: cramos 29/may/2022

# Example 1
print ("\n 1___ For Loop ___")

motorcycles = ['vespa', 'yamaha', 'suzuki', 'triumph', 'honda', 'kawasaki']
for motorcycle in motorcycles:
	print (motorcycle)
	print (f"{motorcycle.title()}, in title format")

# Example 2
print ("\n 2___ Slicing a List ___")
print(motorcycles, '<---- full list')
print(motorcycles[:2], '<----- sliced [:2]')
print(motorcycles[4:], '<----- sliced [4:]')
print(motorcycles[-3:], '<----- sliced [-3:]')

# Example 3
print ("\n 3___ Looping in Sliced List [3:] ___")
print(motorcycles, '<---- full list')
for moto in motorcycles[3:]:
   print(moto.title())
   print(moto.upper())

# Example 4
print ("\n 4___ Copying lists (copy values) ___")
motors = motorcycles[:]
motors.append('Freight-Liner')
print(motorcycles, '<---- motorcycles')
print(motors, '<---- vehicles')

# Example 5
print ("\n 5___ Copying lists (false copy) ___")
vehicles = motorcycles
vehicles.append('Freight-Liner')
print(motorcycles, '<---- motorcycles')
print(vehicles, '<---- vehicles')


# ToDo
# Example 6
print ("\n 6___ ToDo: Creating a two dimensions array [x,y] ___")
