# 오답 코드(추가된 테스트케이스 25번 오답)

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(start, board, visited):
    length = len(board)

    # [r, c, direction, price]
    q = deque()
    q.append(start)
    while q:
        r, c, d, p = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 범위 이탈
            if nr < 0 or nr >= length or nc < 0 or nc >= length:
                continue

            # 벽
            if board[nr][nc] == 1:
                continue

            price = 0 if d == i or d == -1 else 500
            price += (p + 100)

            if visited[nr][nc] and board[nr][nc] < price:
                continue

            q.append((nr, nc, i, price))
            visited[nr][nc] = True
            board[nr][nc] = price


def solution(board):
    # 직선 도로: 100원
    # 코너: 500원
    length = len(board)
    block_list = []
    visited = [[False] * length for _ in range(length)]

    # [r, c, direction, price]
    start = (0, 0, -1, 0)
    bfs(start, board, visited)
    return board[length - 1][length - 1]


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0]]))
# new testcase
print(solution([[0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0]]))
