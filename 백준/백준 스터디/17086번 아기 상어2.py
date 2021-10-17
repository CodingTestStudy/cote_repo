# 효율적이지 않은 방법 #
# 더 좋은 방법이 있을 듯 #


N, M = map(int, input().split())

# 8가지 방향
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

space = [[] for _ in range(N)]
shark = []


def bfs(start_r, start_c):
    q = []
    q.append((start_r, start_c))
    while q:
        sr, sc = q.pop()
        # 8 방향
        for i in range(8):
            nr, nc = sr + dr[i], sc + dc[i]

            # 범위 벗어나는 경우
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 상어를 만난 경우
            if space[nr][nc] in shark:
                continue

            # 처음 방문한 경우, 한 칸 이동
            if space[nr][nc] == 0:
                space[nr][nc] = space[sr][sc] + 1
                q.append((nr, nc))

            # 이전에 방문한 적 있는 경우
            else:
                # 더 작은 값으로
                if space[nr][nc] > space[sr][sc] + 1:
                    space[nr][nc] = space[sr][sc] + 1
                    q.append((nr, nc))


for i in range(N):
    space[i] = list(map(int, input().split()))
    for j in range(M):
        if space[i][j] == 1:
            shark.append((i, j))

for sr, sc in shark:
    bfs(sr, sc)

max_value = 0
for i in range(N):
    for j in range(M):
        if space[i][j] > max_value:
            max_value = space[i][j]
print(max_value - 1)
