"""
List Methods
"""
# list.sort()
color = ["violet", "indigo", "blue", "green"]
color.sort()
print(color)

num = [4, 56, 3, 2, 5, 7, 2, 4]
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print("-------------------------")

# list.append()
num.append(9)
print(num)
print("-------------------------")

# list.reverse()
color = ["violet", "indigo", "blue", "green"]
color.reverse()
print(color)
color = ["violet", "indigo", "blue", "green"]
color = color[::-1]
print(color)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)
num = [4, 2, 5, 3, 6, 1, 2, 1, 2, 8, 9, 7]
num = num[::-1]
print(num)
print("-------------------------")

# list.index()
colors = ["violet", "green", "indigo", "blue", "green"]
print(color.index("violet"))
num = [4, 2, 5, 3, 6, 1, 2, 1, 2, 8, 9, 7]
print(num.index(2))
print("-------------------------")

# list.count()
print(num.count(2))
print(colors.count("green"))
print("-------------------------")

# list.copy()
colors = ["violet", "green", "indigo", "blue", "green"]
rang = colors
rang[1] = "yellow"
print(colors)
print(rang)
"""
As you have seen above, if changes is made in one list 
then it automatically gets reflected in other list of which it was/is a reference
"""

"""
So, in order to avoid such situation we make use of copy() function
copy() : To perform operations on the list without modifying the original list
"""
colors = ["violet", "green", "indigo", "blue", "green"]
rang = colors.copy()
rang[1] = "yellow"
print("\n", "_________Now see the difference by copy() function___________", "\n")
print(colors)
print(rang)
print("-------------------------")

# list.insert()
colors = ["violet", "indigo", "blue"]
#           [0]        [1]      [2]
print(colors)
colors.insert(1, "green")  # insert item at index 1
print(colors)
print("-------------------------")

# list.extend()
colors = ["violet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors = colors + rainbow  # concatenating two lists
print(colors)

colors = ["violet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)  # add a list to a list
print(colors)


