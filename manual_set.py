lst = list(map(int, input().split()))

manual_set = list()

for i in lst:
    if not manual_set.__contains__(i):
        manual_set.append(i)

for i in manual_set:
    print(i, end=' ')
