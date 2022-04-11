import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))
answer = 0
for i in range(1, n + 1):
    for c in combinations(data, i):
        if sum(c) == s:
            answer += 1
print(answer)
