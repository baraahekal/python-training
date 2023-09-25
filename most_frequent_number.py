# A program to get the most frequent number in a list such that -500 <= list[i] <= 270
def find_most_freq(lst):
    freq = [0] * 771

    for i in lst:
        if i > 0:
            freq[i] += 1
        else:
            freq[i + 270 + i * -1 * 2] += 1

    max = -501
    for idx, val in enumerate(freq):
        if (val >= max and idx > 270) or val > max:
            max = val
            pos = idx

    most_freq = pos if pos <= 270 else 270 - pos
    print(most_freq)

if __name__ == '__main__':
    lst = list(map(int, input().split()))
    find_most_freq(lst)





