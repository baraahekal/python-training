def find_smallest(lst, target_type):
    new_lst = [i for i in lst if type(i) is target_type]

    if len(new_lst) == 0:
        return None

    return min(new_lst)


if __name__ == "__main__":
    lst = [10, -2.45, 20, 5, "Mostafa", 5.2, "Ziad"]

    print(find_smallest(lst, type(0)))
    print(find_smallest(lst, type(0.0)))
    print(find_smallest(lst, type("")))
