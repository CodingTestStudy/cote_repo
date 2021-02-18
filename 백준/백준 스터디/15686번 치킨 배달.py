from itertools import combinations
import sys
N, M = map(int, sys.stdin.readline().strip().split())
data = [[] for _ in range(N)]
home = []
chicken_store = []
for i in range(N):
    data[i] = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(N):
        if data[i][j] == 1: home.append((i, j))
        if data[i][j] == 2: chicken_store.append((i, j))

picked_store = list(combinations(chicken_store, M))
distance = [0] * len(picked_store)

for hr, hc in home:
    for j in range(len(picked_store)):
        min_dist = 1e9
        for pr, pc in picked_store[j]:
            dist = abs(hr - pr) + abs(hc - pc)
            min_dist = min(min_dist, dist)
        distance[j] += min_dist

# print(distance)
print(min(distance))


