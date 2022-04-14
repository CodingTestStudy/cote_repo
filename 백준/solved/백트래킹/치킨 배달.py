import sys
from itertools import combinations

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def calculate_distance(r1, r2, c1, c2):
    return abs(r1 - r2) + abs(c1 - c2)


input = sys.stdin.readline
n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

# 0: 빈칸, 1: 집, 2: 치킨집
home = []
store = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            store.append([i, j])

answer = 1e9
for c in combinations(store, m):
    # c: m개의 치킨집
    result = 0
    # 집
    for hr, hc in home:
        distance = 1e9
        # 치킨집
        for cr, cc in c:
            distance = min(distance, calculate_distance(hr, cr, hc, cc))
        result += distance
    answer = min(answer, result)

print(answer)
