def find_lowest_three(lst):
    lst.sort()
    return lst[0:2]

if __name__ == '__main__':
    lst = list(map(int, input().split()))

    min_lst = find_lowest_three(lst)
    print(min_lst)





