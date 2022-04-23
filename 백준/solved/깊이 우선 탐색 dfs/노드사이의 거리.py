import sys
from collections import defaultdict

input = sys.stdin.readline
# n개의 노드, m개의 노드 쌍
n, m = map(int, input().split())
graph = defaultdict(list)
answer_list = [1e9] * m
for _ in range(n - 1):
    start, end, dist = map(int, input().split())
    graph[start].append((dist, end))
    graph[end].append((dist, start))


def dfs(start, end, distance, visited, idx):
    if start == end:
        if answer_list[idx] > distance:
            answer_list[idx] = distance
            return
    else:
        for dist, target in graph[start]:
            if visited[target]:
                continue
            visited[target] = True
            dfs(target, end, distance + dist, visited, idx)
            visited[target] = False


for i in range(m):
    start, end = map(int, input().split())
    visited = [False] * (n + 1)
    dfs(start, end, 0, visited, i)

for i in range(m):
    print(answer_list[i])
