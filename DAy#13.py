# Some String Methods in Python
a = "Ashutosh"  # Strings are immutable (What the F...!, Mind bending concepts)
print(len(a))
a = a.upper()
print(a)
b = "Ashutosh"
print(id(a))
print(id(b))
# upper()
str1 = "AbcDEfghIJ"
print(str1.upper())
# lower()
print(str1.lower())
# strip() ---> removes any white spaces before and after the string
str2 = "   Kise ke pass mall hai   ^O^      "
print(str2.strip())
# rstrip() ---> removes any trailing characters
str3 = "Hello !!!!!!!  !!!!!!!!!"
print(str3.rstrip("!"))
# replace()
print(b.replace("Ashutosh", "HArry"))
# split() ---> splits the given string at the specified instance and returns a list
str2 = "Silver Spoon"
print(str2.split(" "))
# capitalize() ---> turns only first char of string to uppercase and rest to lowercase
blog_Heading = "introduction to Js"
print(blog_Heading.capitalize())
# center() ---> aligns the string to the centre as per parameter
print(str1.center(1))
print(str1.center(13))
print(str1.center(50))
print(str1.center(50, "."))
# count() ---> no of times given is found
str4 = "Abra ka dabra"
print(str4.count("bra"))
print("********** (^O^) **********")
# endswith() ---> returns a boolean
print(str3.endswith("!!!!!!!!!"))
print(str3.endswith(" !!!!!!!!!"))
print(str3.endswith("!!!!!!!!!!"))
"""
you can also check for any in-between value
"""
print("********** (^O^) **********")
str5 = "ola ola ola ola olalalila olalalila olalalila"
print(str5.endswith("ola", 1, 7))
print(str5.endswith("ola", 15, 25))
str5 = "Wel come to the Console !!!"
print(str5.endswith("come", 0,8))
print("********** (^O^) **********")
# find() ---> returns index for the first occurrence of value in the string, not found -1
str5 = 'olalalila olalalila olalalila ola ola ola ola'
print(str5.find("ola"))
str5 = '     olalalila olalalila olalalila ola ola ola ola'
print(str5.find("ola"))
sentence = "He's name is Dan. He is an Honest Man."
print(sentence.find("Daniel"))  # ---> "Daniel" not found hence returned -1
print("********** (^O^) **********")
# index() ---> returns index of the given value but unlike find() raises exception if value not found
print(str1.index("AbcD"))
print(str1.index("c"))
print(str1.index("cD"))
print(str1.index("f"))
# print(str1.index("G")) ---> Throws error because no such "G" letter/String is not present
# isalnum() ---> true if string has A-Z, a-z, 0-9. Else False
str5 = "Welcome to the Console !!!"
print(str5.isalnum())
str5 = "WelcomeToTheConsole00054"
print(str5.isalnum())
print("********** (^O^) **********")
# isalpha() ---> true if string has A-Z, a-z. Else False
print(str5.isalpha())
str5 = "WelcomeToTheConsole"
print(str5.isalpha())
print("********** (^O^) **********")
# islower() ===>> true if all char are lowercase
print(str1)
print(str1.islower())
print(str1.lower())
print((str1.lower()).islower())
print("********** (^O^) **********")
# isprintable() ---> true if all values are printable
sample = "hello, we wish you a \"Merry Christmas\""
print(sample.isprintable())
sample = "hello, we wish you a \n \"Merry Christmas\""
print((sample.isprintable()))
sample = "hello, we wish you a \t \"Merry Christmas\""
print(sample.isprintable())
print("********** (^O^) **********")
# isspace() ---> returns true only and only if string contains white spaces, else false
str5 = '     olalalila olalalila olalalila ola ola ola ola'
print(str5.isspace())
space = "      "  # using spacebar
print(space.isspace())
space = "       "  # using tab
print(space.isspace())
print("********** (^O^) **********")
# istitle() ---> returns true if frst letter of each word is capitalized
str1 = "World Health Organisation"
print(str1.istitle())
str1 = "To kill a Mocking bird"
print(str1.istitle())
print("********** (^O^) **********")
# isupper() ---> opposite of islower()
# startswith() ---> opposite of endswith()
# swapcase() ---> upper to lower, vice versa
str1 = "AbcDEfghIJ"
print(str1.swapcase())
print("********** (^O^) **********")
# title() ---> capitalize starting alphabet of each letter in a string
sentence = "He's name is Dan. He is an Honest Man."
print(sentence.title())