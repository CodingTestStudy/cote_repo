# heapq(우선순위큐)을 활용한 다익스트라

import heapq


def solution(board):
    length = len(board)
    price = [[[1e9] * 4 for _ in range(length)] for _ in range(length)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # (p, r, c, d)
    q = [(0, 0, 0, -1)]
    price[0][0] = [0, 0, 0, 0]
    while q:
        # price 가 작은 순으로 pop()
        p, r, c, d = heapq.heappop(q)

        # 처음이 아니고 이전에 방문한 적 있다면, 최소값으로 지정되어있기 때문에 다루지 않음
        if d != -1 and price[r][c][d] != p:
            continue

        # 도착했다면 가장 작은 값이 도달했기 때문에 바로 return
        if r == length - 1 and c == length - 1:
            return p

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 범위 이탈 or 벽
            if nr < 0 or nr >= length or nc < 0 or nc >= length:
                continue
            # 벽
            if board[nr][nc] == 1:
                continue

            temp = 100 if d == -1 or d == i else 600
            if price[nr][nc][i] > p + temp:
                price[nr][nc][i] = p + temp
                heapq.heappush(q, (temp + p, nr, nc, i))


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

# 오답 코드(추가된 테스트케이스 25번 오답)
#
# from collections import deque
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
#
# def bfs(start, board, visited):
#     length = len(board)
#
#     # [r, c, direction, price]
#     q = deque()
#     q.append(start)
#     while q:
#         r, c, d, p = q.popleft()
#
#         for i in range(4):
#             nr, nc = r + dr[i], c + dc[i]
#
#             # 범위 이탈
#             if nr < 0 or nr >= length or nc < 0 or nc >= length:
#                 continue
#
#             # 벽
#             if board[nr][nc] == 1:
#                 continue
#
#             price = 0 if d == i or d == -1 else 500
#             price += (p + 100)
#
#             if visited[nr][nc] and board[nr][nc] < price:
#                 continue
#
#             q.append((nr, nc, i, price))
#             visited[nr][nc] = True
#             board[nr][nc] = price
#
#
# def solution(board):
#     # 직선 도로: 100원
#     # 코너: 500원
#     length = len(board)
#     block_list = []
#     visited = [[False] * length for _ in range(length)]
#
#     # [r, c, direction, price]
#     start = (0, 0, -1, 0)
#     bfs(start, board, visited)
#     return board[length - 1][length - 1]
