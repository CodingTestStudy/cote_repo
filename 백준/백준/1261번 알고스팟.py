import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
maze = []
answer = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
distance = [[-1] * m for _ in range(n)]

for _ in range(n):
    maze.append(list(map(int, input().strip())))

q = deque()
q.append((0, 0))
distance[0][0] = 0
while q:
    r, c = q.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        # 범위 이탈
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue

        # 첫 방문
        if distance[nr][nc] == -1:
            # 빈 공간인 경우
            if maze[nr][nc] == 0:
                # 가중치 그대로
                distance[nr][nc] = distance[r][c]
                # 빈 공간인 경우 -> 벽을 부수지 않아도 되므로
                # 순서 우선순위를 주기 위해 appendleft()
                q.appendleft((nr, nc))
            # 벽인 경우
            else:
                # 가중치 추가
                distance[nr][nc] = distance[r][c] + 1
                q.append((nr, nc))

print(distance[n - 1][m - 1])
