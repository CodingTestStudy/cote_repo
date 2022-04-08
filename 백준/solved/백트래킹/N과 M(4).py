import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
n, m = map(int, input().split())
combination = list(combinations_with_replacement([i for i in range(1, n + 1)], m))
for comb in combination:
    for c in comb:
        print(c, end=' ')
    print()
