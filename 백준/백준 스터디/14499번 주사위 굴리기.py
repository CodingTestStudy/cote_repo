import sys
N, M, x, y, K = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
order = list(map(int, sys.stdin.readline().strip().split()))
dice = [0 for _ in range(6)]
# 동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 0 : 바닥, 5 : 위
for i in range(K):
    d = order[i] - 1
    nx = x + dx[d]
    ny = y + dy[d]
    if not(0 <= nx < N and 0 <= ny < M): continue

    if d == 0:
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif d == 1:
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif d == 2:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    else:
        dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]

    if board[nx][ny] == 0:
        board[nx][ny] = dice[0]
    else:
        dice[0] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny
    print(dice[5])

