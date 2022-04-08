import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
member = [i for i in range(n)]

s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

permutation = list(combinations(member, n // 2))

min_diff = 1e9
for i in range(len(permutation) // 2):
    s_score, l_score = 0, 0
    per = permutation[i]
    start = list(per)
    link = [i for i in range(n) if i not in start]

    start_combi = list(combinations(start, 2))
    link_combi = list(combinations(link, 2))
    for j in range(len(start_combi)):
        s1, s2 = start_combi[j]
        l1, l2 = link_combi[j]
        s_score += s[s1][s2] + s[s2][s1]
        l_score += s[l1][l2] + s[l2][l1]
    min_diff = min(min_diff, abs(s_score - l_score))
print(min_diff)