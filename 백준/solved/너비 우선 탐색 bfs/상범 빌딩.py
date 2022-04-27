import sys
from collections import deque

input = sys.stdin.readline
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def is_success(time):
    print(f"Escaped in {time} minutes(s)")


def is_fail():
    print("Trapped!")


def bfs(start_z, start_r, start_c, building, visited):
    visited[start_z][start_r][start_c] = 1
    q = deque()
    q.append((start_z, start_r, start_c))
    while q:
        z, r, c = q.popleft()
        for i in range(6):
            nr, nc, nz = r + dr[i], c + dc[i], z + dz[i]
            if 0 <= nr < R and 0 <= nc < C and 1 <= nz <= L:
                if building[nz][nr][nc] == 'E':
                    is_success(visited[z][r][c])
                    return
                if building[nz][nr][nc] == '.' and visited[nz][nr][nc] == 0:
                    q.append((nz, nr, nc))
                    visited[nz][nr][nc] = visited[z][r][c] + 1
    is_fail()


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    building = [[[] * C for _ in range(R)] for _ in range(L + 1)]
    for i in range(1, L + 1):
        building[i] = [list(input().strip()) for _ in range(R)]
        input()

    visited = [[[0] * C for _ in range(R)] for _ in range(L + 1)]

    for z in range(1, L + 1):
        for r in range(R):
            for c in range(C):
                if building[z][r][c] == 'S':
                    bfs(z, r, c, building, visited)
