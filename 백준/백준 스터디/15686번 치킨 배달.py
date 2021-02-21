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

# M개의 치킨집 리스트 (조합 사용)
picked_store = list(combinations(chicken_store, M))
distance = [0] * len(picked_store) # 치킨집 리스트들에 대한 거리 리스트

for hr, hc in home: # 모든 집에 대해서
    for j in range(len(picked_store)): # M개의 치킨집 리스트들에 대해서
        min_dist = 1e9
        for pr, pc in picked_store[j]:
            dist = abs(hr - pr) + abs(hc - pc)
            min_dist = min(min_dist, dist)
        # j번째 치킨집 리스트에서 각 집으로의 거리 중 최소거리 축적
        distance[j] += min_dist

print(min(distance))


