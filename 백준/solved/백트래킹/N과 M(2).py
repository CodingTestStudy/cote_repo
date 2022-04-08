from itertools import combinations

n, m = map(int, input().split())
combination = list(combinations([i for i in range(1, n + 1)], m))
for combi in combination:
    for comb in combi:
        print(comb, end=' ')
    print()
