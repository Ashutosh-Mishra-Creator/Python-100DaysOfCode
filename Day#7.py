num1 = input(print("enter the value of first no:"))
num2 = input(print("enter the value of second no: "))
operation = input(print("enter the type of operation you want to perform: "))


def function1():
    if type(num1) == int and type(num2) == int and operation == "multiplication":
        print("The addition of two number is: ", int(num1) * int(num2))
    elif type(num1) == int and type(num2) == int and operation == "addition":
        print("The addition of two number is: ", num1 + num2)
    else:
        print("wrong inputs")


function1()
