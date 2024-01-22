def average(a=9, b=1):
    print("the average is", (a + b) / 2)


average(4, 9)
average(b=9)


def name(fname, mname = "John", lname = "Whatson"):
    print("Hello,", fname, mname, lname)


name("Anthony")
name("Amy", "Agrawal")
name("Amy", "Agrawal", "Jain")


def average(a, b, c=1):
    print("The average is", (a + b + c)/2)


average(5, 6)


def name(*name):
    print("Hello", end=" ")
    for i in name:
        print(i, end=" ")
    print(end="\n")


name("James", "Duggal", "Manoj", "Barnes", "Buchanan")


def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum += i
    print("Average is", sum/len(numbers))


average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

name = {"fname": "James", "mname": "Buchanan", "lname": "Barnes"}
# ☝ not used in names(**name)


def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="bich", fname="vo", lname="hai")
