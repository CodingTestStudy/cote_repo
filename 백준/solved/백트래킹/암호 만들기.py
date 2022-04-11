import sys
from itertools import combinations

input = sys.stdin.readline

l, c = map(int, input().split())
s = list(input().split())
s.sort()

# 최소 1개의 모음과 최소 2개의 자음
vowel = ['a', 'e', 'i', 'o', 'u']

for combi in combinations(s, l):
    vowel_cnt = 0
    consonant_cnt = 0
    for c in combi:
        if c in vowel:
            vowel_cnt += 1
        else:
            consonant_cnt += 1

    if vowel_cnt >= 1 and consonant_cnt >= 2:
        print(''.join(combi))
