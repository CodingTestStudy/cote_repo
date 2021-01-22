import sys
from collections import deque

input = sys.stdin.readline
move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]


def bfs(length, start_r, start_c, end_r, end_c):
    visited = [[False] * length for _ in range(length)]
    count = 0
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = True
    while q:
        q_length = len(q)
        for _ in range(q_length):
            r, c = q.popleft()
            if r == end_r and c == end_c:
                return count
            for j in range(8):
                nr = r + move[j][0]
                nc = c + move[j][1]
                if 0 <= nr < length and 0 <= nc < length and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
        count += 1


N = int(input())
L = []
before = []
after = []
for _ in range(N):
    L.append(int(input()))
    before.append(list(map(int, input().split())))
    after.append(list(map(int, input().split())))

for i in range(N):
    print(bfs(L[i], before[i][0], before[i][1], after[i][0], after[i][1]))
