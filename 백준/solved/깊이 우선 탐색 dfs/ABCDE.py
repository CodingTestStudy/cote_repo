import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(idx, cnt):
    if cnt == 4:
        print(1)
        exit()

    for friend in graph[idx]:
        if not visited[friend]:
            visited[friend] = True
            dfs(friend, cnt + 1)
            visited[friend] = False


visited = [False] * n
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
print(0)
