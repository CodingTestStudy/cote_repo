import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
permutation = permutations(data, n)

answer = 0
for p in permutation:
    result = 0
    for i in range(n - 1):
        result += abs(p[i] - p[i + 1])
    answer = max(answer, result)
print(answer)
