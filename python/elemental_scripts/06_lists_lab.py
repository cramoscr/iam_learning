# lists_lab.py
# Based on Python Crash Course book (page 37)
# Updated: cramos 13/may/2022

# Example 1
print ("\n 1___ Basic list's handling ___")

motorcycles = ['vespa', 'yamaha', 'suzuki', 'triumph', 'honda', 'kawasaki']
print(motorcycles)

# Example 2
print ("\n 2___ Showing the list's lenght ___")
print(len(motorcycles))

# Example 3
print ("\n 3___ Adding element at [1] possition ___")
motorcycles[1] = 'bmw'
print(motorcycles)

# Example 4
print ("\n 4___ Appending at the end (rightest possition ___")
motorcycles.append('ducati')
print(motorcycles)

# Example 5
print ("\n 5___ Appending using INSERT at possiton 2 ___")
motorcycles.insert(2, 'harley davidson')
print(motorcycles)

# Example 6
print ("\n 6___ Removing with DEL at possiton 2 ___")
del motorcycles[2]
print(motorcycles)
print(motorcycles[2], '<----- motorcycles[2] ')

# Example 7
print ("\n 7___ Removing with POP (rightest possition)___")
motorcycles.pop()
print(motorcycles)

# Example 8
print ("\n 8___ Removing with POP at possition 0 ___")
removed = motorcycles.pop(0)
print(motorcycles)
print(removed, '<----- removed ')

# Example 9
# Tip: remove only deletes the first ocurrence (need a loop a complete searching)
print ("\n 9___ Removing 'suzuki' with REMOVE by searching ___")
motorcycles.remove('suzuki')
print(motorcycles)

# Example 10
# Tip: Uppercase values are ordered at first possition
print ("\n 10___ Sorting ___")
motorcycles.sort()
print(motorcycles)

# Example 11
print ("\n 11___ Sorting (reverse order) ___")
motorcycles.sort(reverse=True)
print(motorcycles)

# Example 12
print ("\n 12___ Reverse sort using reverse() ___")
motorcycles.reverse()
print(motorcycles)

# Example 13
print ("\n 13___ Showing content in a sorted way SORTED() ___")
print(sorted(motorcycles))
print(motorcycles, '<---- Actual order' )

# Example 14
print ("\n 14___ Getting the last item in a list 'using [-1]' ___")
print(motorcycles[-1], '<---- last item' )

