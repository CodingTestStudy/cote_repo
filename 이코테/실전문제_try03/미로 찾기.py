from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 오른쪽 아래
# dx = [0, 1]
# dy = [1, 0]

def bfs(board, x, y):
    q = deque()
    q.append((x, y))
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            if not (0 <= nx + dx[i] < n) or not (0 <= ny + dy[i] < m):
                continue
            if board[nx + dx[i]][ny + dy[i]] == 0:
                continue
            if board[nx + dx[i]][ny + dy[i]] == 1:
                board[nx + dx[i]][ny + dy[i]] = board[nx][ny] + 1
                q.append((nx + dx[i], ny + dy[i]))


bfs(board, 0, 0)
print(board)
print(board[n - 1][m - 1])
