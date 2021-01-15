# 음료수 얼려 먹기
n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(board, x, y):
    if not(0 <= x < n) or not(0 <= y < m):
        return False
    if board[x][y] == 0:
        board[x][y] = 1
        for i in range(4):
            dfs(board, x + dx[i], y + dy[i])
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            dfs(board, i, j)
            result += 1


print(result)