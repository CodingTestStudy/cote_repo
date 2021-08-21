from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    q = deque()
    q.append((r, c))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 0:
                    continue

                if graph[nr][nc] == 1:
                    q.append((nr, nc))
                    graph[nr][nc] = graph[r][c] + 1
    return graph[N - 1][M - 1]
print(bfs(0, 0))
print(graph)
