import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    parent, child, dist = map(int, input().split())
    graph[parent].append(((child, dist)))
    graph[child].append((parent, dist))


def dfs(v, d):
    for vertex, dist in graph[v]:
        if distance[vertex] == -1:
            distance[vertex] = d + dist
            dfs(vertex, d + dist)


distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)
start = distance.index(max(distance))
# print(f"start = {start}")
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)
end = distance.index(max(distance))
# print(f"end = {end}")
print(distance[end])