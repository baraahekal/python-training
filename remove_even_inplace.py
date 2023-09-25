def rmv_evens(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 2 == 0:
            del lst[i]

    print(lst)
if __name__ == '__main__':
    lst = list(map(int, input().split()))
    rmv_evens(lst)





