a = int(input("Enter your age: "))
print("your age is:", a)
# Conditional Operators ---> (=,>,<,>=,<=,==,!=)
print(a > 18)
print(a < 18)
print(a == 18)
print(a != 18)
print(a >= 18)
print(a <= 18)

# if-else Statements
'''
1) if
2) if-else
3)if-else-elif
4) nested if-else-elif
'''

if a > 20:
    b = True

# Program to check if you are eligible to drive any vehicle
if a >= 18:
    print("You can drive")
else:
    print("You cannot drive")
"""
OR
"""
# Program to decide whether to add Apples into the cart or not
applePrice = 210
budget = 200
if applePrice >= budget:
    print("Alexa, do not add apples to the cart")
else:
    print("Alexa, add 1 kg Apples to the cart")

# program to check whether the no, is positive, zero or negative
num = int(input("Enter any whole no."))
if num < 0:
    print("it, is a negative number")
elif num == 0:
    print("it, is a zero")
elif num == 999:
    print("it, is a special number")
else:
    print("it, is a negative number")
print("I am Happy now!")

# program to find out the range of number
if num < 0:
    print("Number is negative")
elif num > 0:
    if 1 <= num <= 10:
        print("Number is between 1-10")
    elif 10 < num <= 20:
        print("the number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("Number is zero")
