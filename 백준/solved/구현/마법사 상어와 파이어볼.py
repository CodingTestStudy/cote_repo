N, M, K = map(int, input().split())

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

ball_info = []
board = [[[] for _ in range(N)] for _ in range(N)]
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    ball_info.append([r - 1, c - 1, m, s, d])

for _ in range(K):
    while ball_info:
        r, c, m, s, d = ball_info.pop()
        nr = (r + s * dr[d]) % N
        nc = (c + s * dc[d]) % N
        board[nr][nc].append([m, s, d])

    for r in range(N):
        for c in range(N):
            if len(board[r][c]) > 1:
                nm, ns, odd, even, cnt = 0, 0, 0, 0, len(board[r][c])
                while board[r][c]:
                    m, s, d = board[r][c].pop()
                    nm += m
                    ns += s
                    if d % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                if odd == cnt or even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if nm // 5 != 0:
                    for d in nd:
                        ball_info.append([r, c, nm // 5, ns // cnt, d])

            if len(board[r][c]) == 1:
                ball_info.append([r, c] + board[r][c].pop())
print(sum(a[2] for a in ball_info))
