import sys
N, M = map(int, sys.stdin.readline().strip().split())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
min_count = 1e9

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
d = [0,
     [[0], [1], [2], [3]],
     [[0, 1], [2, 3]],
     [[1, 2], [1, 3], [0, 2], [0, 3]],
     [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
     [[0, 1, 2, 3]]
     ]

def dfs(start, data, cctv):
    global min_count
    if start == len(cctv):
        cnt = 0
        for r in range(N):
            for c in range(M):
                if data[r][c] == 0:
                    cnt += 1
        # print(min_count, cnt)
        min_count = min(min_count, cnt)
        return

    num, r, c = cctv[start]
    for dir in d[num]:
        temp = [x[:] for x in data]
        for i in dir:
            nr, nc = r + dr[i], c + dc[i]
            while 0 <= nr < N and 0 <= nc < M:
                if temp[nr][nc] == 6: break
                elif temp[nr][nc] == 0:
                    temp[nr][nc] = '#'
                nr += dr[i]
                nc += dc[i]
        dfs(start + 1, temp, cctv)

cctv = []
for r in range(N):
    for c in range(M):
        if data[r][c] not in [0, 6]:
            cctv.append([data[r][c], r, c])
dfs(0, data, cctv)
print(min_count)