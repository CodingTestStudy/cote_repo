import sys

q = []
N = int(sys.stdin.readline().strip())
visited = [[False] * N for _ in range(N)]
space = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
for i in range(N):
    flag = False
    for j in range(N):
        if space[i][j] == 9:
            q = [[i, j]]
            space[i][j] = 0
            visited[i][j] = True
            flag = True
            break
    if flag:
        break

def level_up():
    global shark_size, shark_eat
    if shark_eat == 0:
        shark_size += 1
        shark_eat = shark_size
    return


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
distance = 0
result = 0
shark_size, shark_eat = 2, 2
while q:
    distance += 1
    eaten = []
    for _ in range(len(q)):
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]         
            if not(0 <= nr < N) or not(0 <= nc < N): continue
            if space[nr][nc] > shark_size: continue
            if visited[nr][nc]: continue
            if 0 < space[nr][nc] < shark_size:
                visited[nr][nc] = True
                eaten.append([nr, nc])
            if space[nr][nc] == shark_size or space[nr][nc] == 0:
                visited[nr][nc] = True
                q.append([nr, nc])

    if eaten:
        er, ec = N - 1, N - 1
        for e in eaten:
            if e[0] < er:
                er, ec = e[0], e[1]
            elif e[0] == er:
                if e[1] < ec:
                    ec = e[1]

        shark_eat -= 1
        level_up()
        q = [[er, ec]]
        result += distance
        distance = 0
        space[er][ec] = 0
        visited = [[False] * N for _ in range(N)]
        visited[er][ec] = True
print(result)