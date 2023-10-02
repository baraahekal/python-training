def print_sliding_window(lst):
    start = 0
    end = 3

    while end <= len(lst):
        sub_sum = sum(lst[start:end])
        print(lst[start : end], '=>', sub_sum)
        start += 1
        end += 1


if __name__ == '__main__':
    lst = [1, 0, 3, -4, 2, -6, 9]
    print_sliding_window(lst)
