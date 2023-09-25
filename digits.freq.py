def print_digits_freq(lst):
    freq = [0] * 10

    for val in lst:
        freq[val] += 1

    for idx, val in enumerate(freq):
        print(f"Digit {idx} repeated {val}")

if __name__ == '__main__':
    lst = list(map(int, input().split()))
    print_digits_freq(lst)





