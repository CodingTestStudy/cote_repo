import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

l_list = []

for r in range(n):
    for c in range(m):
        if board[r][c] == 'L':
            l_list.append((r, c))


answer = 0
for r, c in l_list:
    q = deque()
    q.append((r, c))
    visited = [[-1] * m for _ in range(n)]
    visited[r][c] = 0
    result = 0
    while q:
        rr, cc = q.popleft()
        for i in range(4):
            nr, nc = rr + dr[i], cc + dc[i]
            # 범위 이탈
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            # 바다인 경우 + 방문한 경우
            if board[nr][nc] == 'W' or visited[nr][nc] != -1:
                continue
            visited[nr][nc] = visited[rr][cc] + 1
            q.append((nr, nc))
            answer = max(answer, visited[nr][nc])
print(answer)