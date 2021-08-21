N, M = map(int, input().split())

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    if not (0 <= r < N and 0 <= c < M):
        return False
    if graph[r][c] == 0:
        graph[r][c] = 1
        for d in range(4):
            dfs(r + dr[d], c + dc[d])
        return True
    return False


graph = []
for i in range(N):
    graph.append(list(map(int, input())))
result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)
