import sys
from itertools import combinations

input = sys.stdin.readline
s = []
while True:
    data = input().split()

    if len(data) == 1:
        break

    for i in combinations(data[1:], 6):
        print(" ".join(i))
    print()
