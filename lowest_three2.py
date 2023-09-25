def find_lowest_three(lst):
    lst.sort()
    return lst[0:2]

if __name__ == '__main__':
    lst = list(map(int, input().split()))
    print(find_lowest_three(lst)
)





