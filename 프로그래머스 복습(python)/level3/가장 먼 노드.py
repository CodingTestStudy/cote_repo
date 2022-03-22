from collections import deque


def bfs(start, distance, visited, graph):
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        for g in graph[now]:
            if not visited[g]:
                visited[g] = True
                distance[g] = distance[now] + 1
                q.append(g)


def solution(n, edge):
    answer = 0
    distance = [0 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    bfs(1, distance, visited, graph)
    return distance.count(max(distance))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
