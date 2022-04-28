import sys
from collections import deque

input = sys.stdin.readline
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dl = [0, 0, 0, 0, -1, 1]


def is_success(time):
    print(f"Escaped in {time} minute(s).")


def is_fail():
    print("Trapped!")


def bfs(ll, rr, cc):
    q = deque()
    q.append((ll, rr, cc))
    visited[ll][rr][cc] = 1
    while q:
        l, r, c = q.popleft()
        # if building[l][r][c] == 'E':
        #     is_success(visited[l][r][c])
        #     return
        for i in range(6):
            nl, nr, nc = l + dl[i], r + dr[i], c + dc[i]
            # 범위 검사
            if 1 <= nl <= L and 0 <= nr < R and 0 <= nc < C:
                if building[nl][nr][nc] == 'E':
                    is_success(visited[l][r][c])
                    return
                if building[nl][nr][nc] == '.' and visited[nl][nr][nc] == 0:
                    visited[nl][nr][nc] = visited[l][r][c] + 1
                    q.append((nl, nr, nc))
    is_fail()


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    building = [[[] * C for _ in range(R)] for _ in range(L + 1)]
    visited = [[[0] * C for _ in range(R)] for _ in range(L + 1)]
    for i in range(1, L + 1):
        building[i] = [list(input().strip()) for _ in range(R)]
        input()

    for l in range(1, L + 1):
        for r in range(R):
            for c in range(C):
                if building[l][r][c] == 'S':
                    bfs(l, r, c)
