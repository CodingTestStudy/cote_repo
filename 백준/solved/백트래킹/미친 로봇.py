import sys

input = sys.stdin.readline
n, east, west, south, north = map(int, input().split())
dir = [east, west, south, north]

answer = 0

visited = [[False] * (2 * n + 1) for _ in range(2 * n + 1)]
visited[n][n] = True

# 동서남북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def dfs(r, c, cnt, percentage):
    global answer

    if cnt == n:
        answer += percentage
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        # 방문한 적있다면, 무시 -> 단순한 경로가 아니면 다룰 필요 없기 때문
        if visited[nr][nc]:
            continue
        # 범위 이탈
        if nr < 0 or nr > 2 * n + 1 or nc < 0 or nc > 2 * n + 1:
            continue

        visited[nr][nc] = True
        dfs(nr, nc, cnt + 1, percentage * dir[i] * 0.01)
        visited[nr][nc] = False


dfs(n, n, 0, 1)
print(answer)
