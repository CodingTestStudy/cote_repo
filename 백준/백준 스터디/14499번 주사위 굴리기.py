import sys
N, M, x, y, K = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
order = list(map(int, sys.stdin.readline().strip().split()))
dice = [0 for _ in range(6)]
# 동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 0 : 바닥, 5 : 위
for i in range(K): # 모든 order에 대해서
    d = order[i] - 1 # 실제 방향 index와 맞추기 위해 -1
    nx = x + dx[d]
    ny = y + dy[d]

    # 임시 이동 좌표가 범위를 벗어난다면 continue
    if not(0 <= nx < N and 0 <= ny < M): continue

    # 이동 방향에 따라서, 옆면을 제외한 면들을 방향에 맞춰 swap
    if d == 0:
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif d == 1:
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif d == 2:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    else:
        dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]

    # 이동 좌표의 값이 0이라면 주사위 밑 부분 값 복사
    if board[nx][ny] == 0:
        board[nx][ny] = dice[0]
    # 그렇지 않다면 주사위 밑면에 좌표 값 복사 후, 좌표 값 0으로 초기화
    else:
        dice[0] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny # 이동 좌표 초기화
    print(dice[5]) # 주사위 윗면 값 출력

