tup = (1,)
print(type(tup), tup)
# tup[0] = 90  # Return TypeError: 'tuple' object does not support item assignment
tup = (1, 2, 76, 342, 32, "green", True)
print(tup)
country = ("Spain", "Italy", "India")
print(country[0])
print(country[1])
print(country[2])
print("___________________________")

country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1])  # Similar to
print(country[len(country) - 1])
print(country[-3])
print(country[-4])
print("___________________________")

# Check for item
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")
print("___________________________")

# Printing elements within a particular range
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3: 7])
print(animals[-7:-2])
print("___________________________")

# Printing all element from a given index till the end
print(animals[4:])
print(animals[-4:])
print("___________________________")

# Printing all elements from start to a given index
print(animals[:6])
print(animals[:-3])
print("___________________________")

# Print alternate values
print(animals[::2])
print(animals[-8:-1:2])
