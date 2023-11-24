from text import bold_text

print("*****************Calculator*****************\n")

num1 = int(input("Enter the value of first no: "))
num2 = int(input("Enter the value of second no: "))
print(bold_text("\n___IMPORTANT INSTRUCTIONS___\n"))
print("# Points to be noted:")
print("1. Enter 1 for 'Addition' \n2. Enter 2 for 'Subtraction' \n3. Enter 3 for 'Multiplication' \n", end="")
print("4. Enter 4 for 'Division'")

operation = int(input("Enter the type of operation you want to perform: "))

if type(num1) == int and type(num2) == int and operation == 1:
    print("The subtraction of two number is: ", num1 - num2)
elif type(num1) == int and type(num2) == int and operation == 3:
    print("The multiplication of two number is: ", num1 * num2)
elif type(num1) == int and type(num2) == int and operation == 4:
    print("The division of two number is: ", num1 / num2)
else:
    print("wrong inputs")

