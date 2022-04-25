# 단순 dfs는 시간초과 -> dp 추가 활용해야 함
import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline
# m = 세로, n = 가로
m, n = map(int, input().split())
board = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for _ in range(m):
    board.append(list(map(int, input().split())))

visited = [[-1] * n for _ in range(m)]


def dfs(r, c):
    # 목적지에 도착한 경우
    if r == m - 1 and c == n - 1:
        return 1
    # 이전에 방문한 지역인 경우
    if visited[r][c] != -1:
        return visited[r][c]
    # 첫 방문인 지역은 0으로 처리
    visited[r][c] = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 범위 이탈
        if nr < 0 or nc < 0 or nr >= m or nc >= n:
            continue
        if board[r][c] > board[nr][nc]:
            visited[r][c] += dfs(nr, nc)
    return visited[r][c]


print(dfs(0, 0))
