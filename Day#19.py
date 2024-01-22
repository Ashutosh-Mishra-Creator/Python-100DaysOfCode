# Break and continue statement
for i in range(1, 13):
    if i == 10:
        print("skipped! the", i, "th value")
        continue
    if i == 12:
        break
    print("5 x", i, "=", 5*i)

print("loop to chodkar likal gaya")
i = 5
while True:
    print(i)
    if i == 5:
        break
while i != 5:
    print(i)
