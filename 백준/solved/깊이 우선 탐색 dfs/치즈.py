import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt, time = 0, 0
for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            cnt += 1
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 범위 이탈
        if nr < 0 or nc < 0 or nr >= n or nc >= m:
            continue
        # 방문 여부
        if visited[nr][nc]:
            continue
        if board[nr][nc] == 0:
            visited[nr][nc] = True
            dfs(nr, nc)
        # (r, c) -> (nr, nc) == 빈공간 -> 치즈 /// -> 공기와 한면이 접한 경우
        else:
            board[nr][nc] += 1


def after_remove():
    global cnt
    for r in range(n):
        for c in range(m):
            # 총 2면이 공기와 접하는 경우, 치즈 녹음
            if board[r][c] >= 3:
                board[r][c] = 0
                cnt -= 1
            # 공기와 1면만 접하거나 접하지 않은 경우
            elif board[r][c] > 0:
                board[r][c] = 1
    return board


while cnt != 0:
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    dfs(0, 0)
    board = after_remove()
    time += 1
print(time)