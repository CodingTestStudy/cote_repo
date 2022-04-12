import sys

input = sys.stdin.readline
r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = 0
alpha_set = set()


def dfs(rr, cc, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        nr, nc = rr + dr[i], cc + dc[i]
        # 범위 이탈
        if nr < 0 or nr >= r or nc < 0 or nc >= c:
            continue
        # 이전에 지나온 알파벳
        if board[nr][nc] in alpha_set:
            continue
        alpha_set.add(board[nr][nc])
        dfs(nr, nc, cnt + 1)
        alpha_set.remove(board[nr][nc])


alpha_set.add(board[0][0])
dfs(0, 0, 1)
print(answer)
