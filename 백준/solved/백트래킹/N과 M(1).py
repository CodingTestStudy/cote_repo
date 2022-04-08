from itertools import permutations

# 1~n 중 중복 없이 m개
n, m = map(int, input().split())
per = list(permutations([i for i in range(1, n + 1)], m))
for pe in per:
    for p in pe:
        print(p, end=" ")
    print()

