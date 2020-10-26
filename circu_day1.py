# Last digit
print(123 % 10)

# sum of digits
sum_of_digits = 0
my_nbr = 123
while my_nbr:
    sum_of_digits += my_nbr % 10
    my_nbr = my_nbr // 10
print(sum_of_digits)

# hours and minutes since midnight
N = 570
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

print("n found at: " + str(s.find("n")))

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
print(myString[2])
# second to last
print(myString[-2])
# first five
print(myString[:5])
# all but last 2
print(myString[:-2])
# all even and odd indices
print("Even Steven: " + myString[0::2])
print("Odd Tod: " + myString[1::2])
# reverse string
print(myString[::-1])
# reverse odd indices string
print(myString[::-2])

# control structures
# driver speed
driver_speed = 190
if driver_speed <= 50:
    print('ok')
else:
    points = (driver_speed - 50) // 5
    if points > 12:
        print("License Suspended")
    else:
        print("Points: " + str((driver_speed - 50) // 5))

    # Fizz Buzz
    for i in range(1, 50):
        if i == 30:
            break
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
