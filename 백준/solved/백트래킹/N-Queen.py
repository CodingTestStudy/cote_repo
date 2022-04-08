n = int(input())
answer = 0


def dfs(queens, nxt):
    global answer

    # 해당 열에 이미 퀸이 존재하는 위치라면
    if nxt in queens:
        return

    # 대각선 확인
    for r, c in enumerate(queens):
        h = len(queens) - r
        if nxt == c - h or nxt == c + h:
            return

    queens.append(nxt)

    if len(queens) == n:
        answer += 1
        return

    for i in range(n):
        dfs(queens[:], i)


for i in range(n):
    queens = []
    dfs(queens, i)
print(answer)
