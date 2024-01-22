"""for i in range(3):
    print(i)
i = 0
while i < 3:
    print(i)
    i += 1"""
"""i = 0
while i <= 36:
    i = int(input("Enter a number: "))
    print(i)
print("Done with the loop")
"""
count = 5
while count > 0:
    print(count)
    count = count - 1
else:
    print("I am inside else")

"""while count > 0:
    print(count)  # Infinite while loop
    count = count + 1"""

# Do while loop in not the case with python
"""
do {
    # loop body;    
}while(condition);
"""
# ☝ here whether the condition be true/false, the do-while will execute for one time at least.

# How to emulate a do-while loop
"""The most common technique to emulate do-while loop in python is to use a infinite while loop with a break 
statement wrapped in a if statement that check a given condition and breaks the iteration if that condition becomes 
true"""
# Example of do-while loop
while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 8:
        break
