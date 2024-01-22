marks = [3, 5, 6, 7, 8, 9]
lst2 = ["Red", "Green", "Blue"]
print(marks)
print(lst2)

print(lst2[0])
print(lst2[1])
print(lst2[2])
"""
print(lst2[3])  # list index out of range
"""
# List can contain different types of data types like int, string, boolean, float, etc..
details = ["Abhijeet", 18, "FBI", 9.8, True]
print(details)
print(type(details))
# index in list starts from zero whereas, len(list) = total index count + 1

# Negative Indexing
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])  # negative Index
"""
OR
"""
print(colors[len(colors) - 1])  # positive Index
print(colors[len(colors) - 3])
print(colors[len(colors) - 5])
# Gives the same result as above

# Check whether an item in present in the list?
if "yellow" in colors:
    print("Present")
else:
    print("Absent")

if "Yellow" in colors:
    print("Present")
else:
    print("Absent")

if 9.8 in details:
    print("Present")
else:
    print("Absent")

# Same thing applies for string as well
if "jeet" in "Abhijeet":
    print("Present")
else:
    print("Absent")

"""
Range of Index:
    listName[start : end : jumpIndex]
"""
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	 # using positive indexes
print(animals[-7:-2])  # using negative indexes'
print(animals[len(animals) - 7: len(animals) - 2])  # using positive index

print(animals[4:])
print(animals[-4:])

print(animals[:6])
print(animals[:-3])

print(animals[::2])
print(animals[-8:-1:2])

print(animals[1:8:3])