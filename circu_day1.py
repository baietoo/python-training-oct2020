from datetime import datetime

# Last digit
print(123 % 10)

# sum of digits
sumOfDigits = 0
myNbr = 123
for x in range(len(str(myNbr))):
    sumOfDigits = sumOfDigits + myNbr % 10
    myNbr = myNbr // 10
print(sumOfDigits)

# hours and minutes since midnight
N = 370
hours = N // 60
minutes = N % 60
print(str(hours) + " " + str(minutes))

# STRING EXERCISES
# and in s
s = "bandana"
if "and" in s:
    print(s + " contains the word and.")

# index of n and q
for i in range(len(s)):
    if s[i] == "n":
        print("n found at positon: " + str(i))
    if s[i] == "q":
        print("q found at positon: " + str(i))

# "an" occurences
print("'An' appears in s " + str(s.count("an")) + " time(s).")

# uppercase s
print(s.upper())

# s is alphanumeric
if s.isalnum():
    print("s is alphaNumeric")

# abcdefghijklmn exercises
myString = "abcdefghijklmn"
# third character
print(str(myString[2]))
# second to last
print(myString[-2])
# first five
print(myString[:5])
# all but last 2
print(myString[:-2])
# all even and odd indices
evenSteven = ""
oddTodd = ""
for i in range(len(myString)):
    if i % 2 == 0:
        evenSteven += myString[i]
    else:
        oddTodd += myString[i]
print("Even Steven: " + evenSteven)
print("Odd Tod: " + oddTodd)
# reverse string
print(myString[::-1])
# reverse odd indices string
print(myString[::-2])
