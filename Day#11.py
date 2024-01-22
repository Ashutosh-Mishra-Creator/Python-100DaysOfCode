# Lets study about the strings
name = ("Akshay"
        " how are yoou "
        ""
        "kaise ho "
        "jp"
        ""
        "ya mar gaye")
print(name)

# Multiline string kaise likhte hai kuch idea hai
# chalo mai batata hu
name2 = '''howdy modi
chalo sab ko baulava bhejo
sab chaiye mujhe joe bidon
aur jim pin, putinn, kim jo hun
aur jo koi bhi ahi sab ko bula lo'''
print(name2)

# abb agar ise print karna hai ko kaise karre :- 'he said, "I want to eat an apple".'
# chalo dekhte hai kaise karna binna kissi error ke
'''
texting = 'He said,
"I want to eat an apple".'            ---->> This will throw an error, so in order to tacle this we can do this.
print(texting)
'''

texting = '''\nhe said,
"I want to eat an apple".'''           # Thus we can use ''' ''' as a way to write multiple paragraph and print as it
print(texting)

# Escape Characters

# txt = "We are the so-called "Vikings" from the north."
txt2 = "We are the so-called \"Vikings\" from the north."  # Dekha kaise bhaga diya " ko

# Accessing Characters of String
print(txt2[0])
print(txt2[1])
print(txt2[2])
print(txt2[3])
print(txt2[4])
print(txt2[5])
print(txt2[6])
print(txt2[7])
print(txt2[8])
print(txt2[9])
print(txt2[10])

print("Lets use a for loop\n")

# Looping the string
for char in txt2:
    print(char)

# to bhai log kaisa laga ajj ka session, jakas na to like share thoko daba ke


