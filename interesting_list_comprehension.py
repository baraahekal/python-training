lst = [-6, 2, 3, -2, 0, 5, -3, 8]

# Copying the whole [lst] into [copy_lst]
copy_lst = [element for element in lst]
print(copy_lst) # [-6, 2, 3, -2, 0, 5, -3, 8]


# Appending only +ve numbers to [lst1]
lst1 = [element for element in lst if element > 0]
print(lst1) # [2, 3, 5, 8]


# Appending only even numbers to [lst2]
lst2 = [element for element in lst if element % 2 == 0]
print(lst2) # [-6, 2, -2, 0, 8]


# Appending every vowel letter in (sentence) to [vowels]
sentence = "Glad to see you here again!"
vowels = [letter for letter in sentence if letter in "aeiou"]
print(vowels) # ['a', 'o', 'e', 'e', 'o', 'u', 'e', 'e', 'a', 'a', 'i']


def mul(n) -> int:
    return 2 * n


def is_even(n) -> bool:
    return n % 2 == 0

# Appending only double of even numbers using functions
lst3 = [mul(i) for i in lst if is_even(i)]
print(lst3) # [-12, 4, -4, 0, 16]
