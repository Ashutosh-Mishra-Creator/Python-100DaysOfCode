# from time import gmtime, strftime
from datetime import datetime

# s = strftime("%a, %d %b %Y %H:%M:%S")
# print(s)

now = datetime.now()
# s = today.strftime("%a, %d %b %Y %H:%M:%S")
a = int(now.strftime("%H"))
print(a)
if 8 <= a < 12:
    print("Good Morning!")
elif a == 12:
    print("Good Noon")
elif 12 < a < 6:
    print("Good AfterNoon")
elif 6 <= a < 10:
    print("Good Evening")
else:
    print("Good Night")
