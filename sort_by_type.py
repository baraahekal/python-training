def most_freq(lst):
    dct = {}

    for i in lst:
        dct.setdefault(type(i), [])
        dct[type(i)].append(i)

    return [sorted(dct[key]) for key in dct]


if __name__ == '__main__':
    lst = [10, "most", 2.3, 7, "aly", 9, 4.5, 2, "ziad", -4, 1.1, [1, 5], 5, [0, 7, 8]]
    print(most_freq(lst))