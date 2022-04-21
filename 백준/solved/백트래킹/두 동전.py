import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
for r in range(n):
    board.append(list(input().strip()))

coins = []
for r in range(n):
    for c in range(m):
        if board[r][c] == 'o':
            coins.append((r, c))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = []


def check_range(r, c):
    if r < 0 or c < 0 or r >= n or c >= m:
        return False
    return True


def bfs(row1, column1, row2, column2, count):
    q = deque()
    q.append((row1, column1, row2, column2, count))
    while q:
        r1, c1, r2, c2, cnt = q.popleft()
        if cnt >= 10:
            return -1
        for i in range(4):
            nr1, nc1 = r1 + dr[i], c1 + dc[i]
            nr2, nc2 = r2 + dr[i], c2 + dc[i]

            if check_range(nr1, nc1) and check_range(nr2, nc2):
                if board[nr1][nc1] == '#':
                    nr1, nc1 = r1, c1
                if board[nr2][nc2] == '#':
                    nr2, nc2 = r2, c2
                if nr1 == nr2 and nr2 == nc2:
                    continue
                q.append((nr1, nc1, nr2, nc2, cnt + 1))
            elif check_range(nr1, nc1):
                return cnt + 1
            elif check_range(nr2, nc2):
                return cnt + 1
            else:
                continue


answer = bfs(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)
print(answer)
