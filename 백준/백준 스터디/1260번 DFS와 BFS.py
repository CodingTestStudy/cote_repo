import sys
from collections import deque
sys.setrecursionlimit(10000)

def dfs(array, v, visited):
    print(v, end=' ')
    visited[v] = True
    array[v].sort() # 여러군데 방문 가능한 경우, 정점 번호 작은 것 먼저 방문하기 위해 정렬
    for value in array[v]:
        if not visited[value]:
            dfs(array, value, visited)

def bfs(array, v, visited):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        data = q.popleft()
        print(data, end=' ')
        for value in array[data]:
            if not visited[value]:
                q.append(value)
                visited[value] = True


# N : 정점의 개수, M : 간선의 개수, V : 탐색할 정점의 번호
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    # 간선이 양방향이기 때문에 둘다 append()
    graph[start].append(end)
    graph[end].append(start)

dfs(graph, V, visited1)
print()
bfs(graph, V, visited2)