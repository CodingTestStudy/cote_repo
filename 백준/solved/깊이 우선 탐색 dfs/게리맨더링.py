import sys
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
# area -> 각 구의 인구수
area = [0]
area.extend(list(map(int, input().split())))
# graph -> 각 구 끼리의 연결 관계 리스트
graph = [set() for _ in range(n + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for ar in data[1:]:
        graph[i].add(ar)
        graph[ar].add(i)


def bfs(temp):
    start = temp[0]
    q = deque()
    q.append(start)
    visited = set()
    visited.add(start)
    total = 0
    while q:
        target = q.popleft()
        total += area[target]
        for nxt in graph[target]:
            if nxt not in visited and nxt in temp:
                visited.add(nxt)
                q.append(nxt)
    return total, len(visited)


result = 1e9
for cnt in range(1, (n // 2) + 1):
    for combi in combinations([i for i in range(1, n + 1)], cnt):
        temp1 = list(combi)
        temp2 = []
        for i in range(1, n + 1):
            if i not in temp1:
                temp2.append(i)

        sum1, len1 = bfs(temp1)
        sum2, len2 = bfs(temp2)

        if len1 + len2 == n:
            result = min(result, abs(sum1 - sum2))

if result == 1e9:
    print(-1)
else:
    print(result)
