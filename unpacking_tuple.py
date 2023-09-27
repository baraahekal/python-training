lst = 1, 2, 3, 4, 5

a, b, c, d, e = lst
a, b, _, _, _ = lst

print(a, b)  # 1 2

# if we don't know the size of tuple:
a, b, *c = lst
print(c)  # [3, 4, 5]


# using * before the argument make the function accepting many passing values
def f(*items):
    print(items)  # (1, 2, 3, 'Ahmed')


f(1, 2, 3, "Ahmed")
