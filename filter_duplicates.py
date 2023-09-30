def filter_duplicates(lst_of_lsts):
    lst_of_tpls = [tuple(lst) for lst in lst_of_lsts]
    return list(dict.fromkeys(lst_of_tpls))


if __name__ == '__main__':
    lst = [[7, 1], [2, 4], [7, 1], [5, 2], [2, 4]]
    print(filter_duplicates(lst))
