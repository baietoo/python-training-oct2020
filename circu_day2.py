# try statement exercises
# Write a program to read two numbers: x and y from standard input and print the result of x / y. If the user inputs invalid data, display an error message and exit gracefully.

x = input('x : ')
y = input('y : ')
try:
    result = int(x) / int(y)
except ArithmeticError as ex:
    print(f"cannot perform division {x} / {y} something went wrong.")
except ValueError as ex:
    print(f"Please ensure you input an integer number. Your input: {x}, {y}.")
else:
    print(f"Result: {x} / {y} = {result}")

# Lists exercises
# Given the following list:
l = [4, 6, 1, 7, 8, 2, 8, 2, 4, 6, 8, 9]
# Add[5, 7, 8] to the end of the list
l.extend((5, 7, 8))
# Print the length of the list
print(f"length of list: {len(l)}.")
# Check if 8 is in the list
print(f"8 within list? {8 in l}.")
# Print the first position of 7 in the list
print(f"first 7 position: {l.index(7)}.")
# Count how many times 8 is in the list
print(f"8 occurences: {l.count(8)}.")
# Reverse the list
print(f"Reversed list: {l[::-1]}.")
# Sort the list
l.sort()
print(f"Sorted list: {l}.")  # l.sort() doesn't work in an f string

# Remove all items on positions divisible by 3
del l[::3]
print(f"list after removing indices div by 3: {l}.")

# Write a Python program to convert a list of characters into a string.
char_list = ['o', 'h', 'n', 'g', ' ', 'a', 'w', 'd']
print(f"Joined list: {''.join(char_list)}.")
# Write a Python program to find the second smallest number in a list.

l = list(dict.fromkeys(l))
l.sort()
print(l)
print(f"second smallest number: {l[1]}.")


# Sets exercises
# Given the following set:

s = set()
# Add elements from [1, 2, 3] to the set
s.update([1, 2, 3])
# Print the length of the set
print(f"Set length: {len(s)}.")
# Check if 4 is in the set
print(f"Is 4 in set? {4 in s}.")
# Remove and print an arbitrary element from the set
print(f"arbitrary elem from set: {s.pop()}")
# Remove all remaining items in the set
s.clear()

# Write a Python program that counts the number of distinct words from a string.
# A word = a sequence of characters that is not whitespace(space, newline, tab).

# E.g.
my_string = """beautiful is better than ugly
explicit is better than implicit
simple is better than complex
complex is better than complicated
flat is better than nested
sparse is better than dense"""
# # Should print: 14 distinct words

oh_my_words = set()
oh_my_words.update(my_string.split())
print(f"length of unique items: {len(oh_my_words)}.")


# Dicts exercises
# Given the following dictionary:

d = {
    'times': 100,
    'name': 'George',
    'hobbies': ['fishing', 'hiking'],
}
# add key 'friends' to d with ['Andrei', 'Mihai', 'Alina'] as value
d["friends"] = ['Andrei', 'Mihai', 'Alina']
# sort value for key 'friends'
d['friends'].sort()
# remove 'hiking' from hobbies list
d["hobbies"].remove('hiking')
# remove 'times' key from d
del d['times']
print(d)
# Given a list of strings build a dictionary that has each unique string as a key and the number of appearances as a value.
# E.g. ['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there'] -> {'hello': 2, 'is': 1, 'there': 2, 'anybody': 1, 'in': 1}
string_list = ['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']
string_dict = {}
for string in string_list:
    string_dict[string] = string_list.count(string)
print(f"Final dictionary: {string_dict}.")
