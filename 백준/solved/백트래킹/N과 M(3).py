import sys
from itertools import product

input = sys.stdin.readline
n, m = map(int, input().split())
pro = list(product([i for i in range(1, n + 1)], repeat=m))
for pr in pro:
    for p in pr:
        print(p, end=' ')
    print()
