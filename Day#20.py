a = 9
b = 8

if a < b:
    print(b, "is greater")
else:
    print(a, "is greater or equal")

gmean1 = (a*b)/(a+b)
print(gmean1)

c = 7
d = 23

if c < d:
    print(d, "is greater")
else:
    print(c, "is greater or equal")

gmean2 = (c*d)/(c+d)
print(gmean2)


def gmean(num1, num2):
    mean = (num1*num2)/(num1+num2)
    print(mean)


def comparision(num1, num2):
    if num1 > num2:
        print(num1, "is greater than", num2)
    elif num2 > num1:
        print(num2, "is greater than", num1)
    else:
        print(num1, ",", num2, "are equal")


gmean(a, b)
gmean(c, d)
comparision(a, b)
comparision(c, d)


def anonymous(num1, num2):
    pass

