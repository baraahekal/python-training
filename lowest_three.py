def find_lowest_three(lst):
    min_lst = [None] * 3
    min_lst[0], min_lst[1], min_lst[2] = lst[0], lst[1], lst[2]
    min_lst.sort()

    for i in range(3, len(lst)):
        if lst[i] < min_lst[0]:
            min_lst[0] = lst[i]
        elif lst[i] < min_lst[1]:
            min_lst[1] = lst[i]
        elif lst[i] < min_lst[2]:
            min_lst[2] = lst[i]
    return min_lst

if __name__ == '__main__':
    lst = list(map(int, input().split()))

    min_lst = find_lowest_three(lst)
    print(min_lst)