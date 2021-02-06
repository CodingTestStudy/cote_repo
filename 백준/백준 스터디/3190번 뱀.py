import sys
from collections import deque
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

snake = deque([1, 1])
head = [1, 1]
d_idx = 0 # 방향 결정 index
d = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
time = -1
nothing_r = -1
nothing_c = -1
Continue = True

while Continue:
    time += 1
    if len(turn) != 0 and turn[0][0] == time: # 방향 전환시간
        x, dd = turn.popleft() # 시간, 방향 (시간은 쓰이지 않음)
        if dd == 'L':
            d_idx = (d_idx + 3) % 4 # 왼쪽으로 회전
        elif dd == 'D':
            d_idx = (d_idx + 1) % 4 # 오른쪽으로 회전

    # 뱀의 머리부분에 대한 데이터를 알기 위해,
    # snake 리스트에서 빼고 head 변수에 할당 후, 다시 넣음
    head = (snake.popleft(), snake.popleft())
    snake.appendleft(head)

    # 벽에 부딪히는 경우
    if not(1 <= head[0] < N + 1) or not(1 <= head[1] < N + 1):
        Continue = False
        break

    # 자기 몸에 부딪히는 경우 1
    for i in range(1, len(snake)):
        if head == snake[i]: # 머리가 snake 리스트 내부에 값과 일치하면
            Continue = False
            break

    # 자기 몸에 부딪히는 경우 2
    # nothing_r, _c 는 이전에 버린 꼬리 좌표이다.
    # 하지만 문제에서는 몸길이를 늘려 머리를 다음칸에 먼저 위치하고,
    # 사과가 존재하면 꼬리 그대로, 사과 없으면 그때서야 꼬리 위치 좌표를 비워준다.
    # 코드 내에서는 꼬리 좌표를 먼저 pop()으로 삭제를 하긴했지만, 해당 데이터 값은 변수에 저장되어 있기 때문에
    # 지난 꼬리 좌표도 몸에 부딪히는지 확인해야 한다.
    for value in snake:
        if nothing_r == value[0] and nothing_c == value[1]:
            Continue = False
            break

    # 방향맞춰 다음 칸을 snake 리스트의 맨앞(머리)에 삽입
    snake.appendleft(head[1] + d[d_idx][1])
    snake.appendleft(head[0] + d[d_idx][0])

    # 사과를 발견한 경우
    if board[snake[0]][snake[1]] == 1:
        board[snake[0]][snake[1]] = 0 # 꼬리 부분을 버리지 연산 X, 사과를 먹었다는 의미로 1을 0으로 바꿔준다.

    # 사과 발견 X
    else:
        nothing_r, nothing_c = snake.pop() # 꼬리 부분을 버린다.

print(time)
