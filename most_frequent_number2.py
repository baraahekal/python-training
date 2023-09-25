# A program to get the most frequent number in a list such that -500 <= list[i] <= 270
def find_most_freq(lst):
    freq = [0] * 771
    shifting = abs(min(lst))

    for i in lst:
        freq[i + shifting] += 1

    most_value = freq.index(max(freq)) - shifting
    print(most_value)


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    find_most_freq(lst)





