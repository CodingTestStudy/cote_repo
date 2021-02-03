import sys
from collections import deque
# import heapq
N = int(input()) # N x N
K = int(input()) # 사과 개수
board = [[0] * (N + 2) for _ in range(N + 2)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().strip().split())
    board[r][c] = 1 # 사과 위치
L = int(input())
turn = deque()
for _ in range(L):
    time, direction = sys.stdin.readline().strip().split()
    turn.append((int(time), direction))

# right, down, left, up
snake = deque([1, 1]) #
head = [1, 1]
d_idx = 0
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
time = -1
nothing_r = -1
nothing_c = -1
Continue = True
while Continue:
    time += 1
    if len(turn) != 0 and turn[0][0] == time: # 방향 전환시간
        # print("방향 전환")
        x, dd = turn.popleft()
        if dd == 'L':
            d_idx = (d_idx + 3) % 4
        elif dd == 'D':
            d_idx = (d_idx + 1) % 4
    head = (snake.popleft(), snake.popleft())
    snake.appendleft(head)
    # print("현재 시간 : ", time)
    # print("현재 뱀 상태 : ", snake)
    # print("현재 머리 : ", head)
    # print("이전에 짤린 꼬리", nothing_r, nothing_c)
    # print()
    for value in snake:
        # print(value, value[0], value[1])
        if nothing_r == value[0] and nothing_c == value[1]:
            # print("자기 몸과 부딪힘")
            Continue = False
            break

    if not(1 <= head[0] < N + 1) or not(1 <= head[1] < N + 1): # 벽에 부딪히는 경우
        # print("범위 벗어남")
        Continue = False
        break

    for i in range(1, len(snake)): # 자기 몸에 부딪히는 경우
        if head == snake[i]:
            # print("자기 몸과 부딪힘")
            Continue = False
            break

    snake.appendleft(head[1] + d[d_idx][1])
    snake.appendleft(head[0] + d[d_idx][0])

    if board[snake[0]][snake[1]] == 1:
        # print(snake[0], snake[1], "에서 사과 발견")
        board[snake[0]][snake[1]] = 0
    else:
        nothing_r, nothing_c = snake.pop()
        board[nothing_r][nothing_c] = 0

print(time)