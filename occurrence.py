lst = list(map(int, input().split()))

freq = [-1] * 501

for i in range(len(lst)):
    freq[lst[i]] = i

queries = list(map(int, input().split()))

for query in queries:
    print(f"Query {query} occurs in position {freq[query]}")