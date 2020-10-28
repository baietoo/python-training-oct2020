import string
numbers = [3, 4, 5]
squared_numbers = [nbr ** 2 for nbr in numbers if nbr % 2 == 0]
print(squared_numbers)
# 1. create dictionary
my_dict = {}
my_dict = {letter: ord(letter)
           for letter in string.ascii_lowercase if letter <= 'e'}
print(my_dict)

# 2. swap keys
my_dict = {k: v for (v, k) in my_dict.items()}
print(my_dict)

# 3. even keys
my_dict = {k: v for (k, v) in my_dict.items() if k % 2 == 0}
print(my_dict)

# 4.
my_dict = {ord(letter): letter for letter in string.ascii_lowercase if letter <=
           'e' and ord(letter) % 2 == 0}
print(my_dict)
