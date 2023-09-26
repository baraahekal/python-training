lst = [-6, 2, 3, -2, 0, 5, -3, 8]

lst1 = [element for element in lst if element > 0]
print(lst1) # [2, 3, 5, 8]

lst2 = [element for element in lst if element % 2 == 0]
print(lst2) # [-6, 2, -2, 0, 8]

sentence = "Glad to see you here again!"
vowels = [vowel for vowel in sentence if vowel in "aeiou"]
print(vowels) # ['a', 'o', 'e', 'e', 'o', 'u', 'e', 'e', 'a', 'a', 'i']

# this new syntax takes every element in [lst] that greater than 0
# and append it to the [new_lst]


def mul(n) -> int:
    return n * n


def is_even(n) -> bool:
    return n % 2 == 0


lst3 = [mul(i) for i in lst if is_even(i)]
print(lst3) # [36, 4, 4, 0, 64]
