"""
The zip() function in Python is used to combine
two or more iterable dictionaries into a single
iterable, where corresponding elements from the
input iterable are paired together as tuples
"""

numbers = [1, 2, 3, 4]  # note number 4
letters = ['B', 'M', 'F']
names = ["Baraa", "Mostafa", "Farouk"]

zipped = zip(numbers, letters)
print(list(zipped))  # [(1, 'B'), (2, 'M'), (3, 'F')]

for tuple_item in zip(numbers, letters, names):
    print(tuple_item)

"""
(1, 'B', 'Baraa')
(2, 'M', 'Mostafa')
(3, 'F', 'Farouk')
"""

for number, letter, name in zip(numbers, letters, names):
    print(number, name, letter)

"""
1 Baraa B
2 Mostafa M
3 Farouk F
"""

