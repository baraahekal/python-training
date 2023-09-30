def most_freq(lst):
    freq = {}

    for i in lst:
        freq.setdefault(i, 0)
        freq[i] += 1

    most = max(freq.values())

    max_lst = [key for key in freq if freq[key] == most]
    print(max_lst)


if __name__ == '__main__':
    lst = map(int, input().split())
    most_freq(lst)