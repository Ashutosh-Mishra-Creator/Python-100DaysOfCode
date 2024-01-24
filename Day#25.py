"""
Operations on Tuple in Python
"""
# Manipulating Tuples
"""
Tuples are immutable, hence if you want to add, remove or change tuple items, 
then first you must convert the tuple to a list. 
Then perform operation on that list and convert it back to tuple.
"""
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
print(temp)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)
print("___________________________")

# We can directly concatenate two tuples without converting them to list.
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
print("___________________________")

# Tuple Methods
# count() --> tuple.count(element)
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
num = Tuple1.count(3)
print(num)
print("___________________________")

# index() --> tuple.index(element, start, end)
res = Tuple1.index(3)
print("Fist occurrence of 3 is", res)
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res = tuple1.index(3, 4, 8)
print(res)
tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.index(3, 4, 8)
print(res)
print("___________________________")

# len()
len(tuple1)
