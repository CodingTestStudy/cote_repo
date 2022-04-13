import sys
from itertools import permutations

input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

for per in permutations(num, m):
    for p in per:
        print(p, end=' ')
    print()
