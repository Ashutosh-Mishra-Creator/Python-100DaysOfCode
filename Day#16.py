x = int(input("Enter some random number: "))
# x is the variable to match
match x:
    case 0:
        print("x is zero")
    case 4 if x % 2 == 0:
        print("x%2 is zero and case is 4")  # case with If condition
    case _ if x < 10:
        print("x is less than (<) 10")
        # default case, runs when none of case is matched
    case _:
        print("The value of x is", x)

