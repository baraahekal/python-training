# <font color='#FFCC70'>List Comprehension in 🐍</font>

List comprehension offers a shorter syntax when you want to create a new list based on the values
of an existing list

## <font color='#8ECDDD'>Example 1:</font>
Say that you need to copy all numbers from a list and
adding +1 to each of them 

#### Normal way:
```python
numbers = [1, 2, 3, 4, 5, 6]

copy_lst = list()

for num in numbers:
    copy_lst.append(num + 1) # [2, 3, 4, 5, 6, 7]
```

#### List Comprehension way:
```python
numbers = [1, 2, 3, 4, 5, 6]

copy_lst = [num + 1 for num in numbers] # [2, 3, 4, 5, 6, 7]
```

## <font color='#8ECDDD'>Example 2:</font>
### (Conditional List Comprehension)
Say that you need to filter all even numbers 
in a list copying them to a new list

#### Normal way:
```python
numbers = [1, 2, 3, 4, 5, 6]

copy_lst = list()

for num in numbers:
    if num % 2 == 0:
        copy_lst.append(num) # [2, 4, 6]
```

#### List Comprehension way:
```python
numbers = [1, 2, 3, 4, 5, 6]

copy_lst = [num for num in numbers if num % 2 == 0] # [2, 4, 6]
```

## <font color='#8ECDDD'>Example 3:</font>
Say that you have a sentence and you need to 
extract all vowel letters from it:
```python
sentence = "Glad to see you here again!"
vowels = [letter for letter in sentence if letter in "aeiou"]
print(vowels) # ['a', 'o', 'e', 'e', 'o', 'u', 'e', 'e', 'a', 'a', 'i']
```
<span style="color:red;">Red Text</span>

## <font color='#8ECDDD'>Example 4:</font>
### Filter and transformation 
> **Warning**
> <font color="red">a Little harder</font>

```python
numbers = [-1, 1, 2, -5, 3, 4, -9, 5]


def is_positive(n) -> bool:
    return  n > 0


def filter(n) -> int:
    return n if n % 2 == 0 else n + 1


copy_lst = [filter(i) for i in numbers if is_positive(i)]
print(copy_lst) # [2, 2, 4, 4, 6, 6]
```