import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline
n = int(input())
grid = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for _ in range(n):
    grid.append(list(input().strip()))

three_cnt, two_cnt = 0, 0

visited = [[False] * n for _ in range(n)]


def dfs(r, c):
    visited[r][c] = True
    color = grid[r][c]
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 범위 이탈
        if nr < 0 or nc < 0 or nr >= n or nc >= n:
            continue
        if not visited[nr][nc] and grid[nr][nc] == color:
            dfs(nr, nc)


for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            dfs(r, c)
            three_cnt += 1

for r in range(n):
    for c in range(n):
        if grid[r][c] == 'G':
            grid[r][c] = 'R'

visited = [[False] * n for _ in range(n)]

for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            dfs(r, c)
            two_cnt += 1

print(three_cnt, two_cnt)
