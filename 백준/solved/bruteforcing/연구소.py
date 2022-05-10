from itertools import combinations
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
zero, virus, zero_cnt, answer = [], [], 0, -1
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            zero.append((r, c))
            zero_cnt += 1
        elif board[r][c] == 2:
            virus.append((r, c))

        # 빈 공간에 대해 3개의 벽을 세울 수 있는 경우의 수
combination = combinations(zero, 3)
for combi in combination:
    result = 0
    temp = deepcopy(board)
    # 벽 생성
    for r, c in combi:
        temp[r][c] = 1

    for rr, cc in virus:
        q = deque()
        q.append((rr, cc))
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if temp[nr][nc] == 0:
                        temp[nr][nc] = -1
                        result += 1
                        q.append((nr, nc))
    answer = max(answer, zero_cnt - result)
# 3개의 벽을 세웠기 때문에 -3
print(answer - 3)
