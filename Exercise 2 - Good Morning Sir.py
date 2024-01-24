from datetime import date
import time
today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))

if hour >= 0 and hour < 12:
    print("Good Morning Sir!")
elif hour >= 12 and hour < 17:
    print("Good Afternoon Sir!")
elif hour>= 17 and hour < 0:
    print("Good Night Sir!")

