lst = 1, 2, 3, (4, 5)

a, b, c, d = lst
print(d) # (4, 5)

# what if we need to unpack all values?
# we need to do a deep unpacking:

a, b, c, (d, e) = lst
print(d) # 4


# very deep unpacking 🤣
t = 1, 2, 3, (4, (5, 6))
a, b, c, (d, (e, f)) = t

print(e, f) # 5, 6
