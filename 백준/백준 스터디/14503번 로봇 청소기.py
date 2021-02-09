import sys
N, M = map(int, sys.stdin.readline().strip().split())
r, c, d = map(int, sys.stdin.readline().strip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph[r][c] = 9 # 현재 위치 청소함
count = 1
Continue = True
turn_count = 0


while Continue:
    nd = (d + 3) % 4 # 왼쪽 회전
    nx, ny = r + dx[nd], c + dy[nd] # 왼쪽 회전 후, 한칸 이동한 임시 좌표
    # a
    if graph[nx][ny] == 0:
        turn_count = 0
        graph[nx][ny] = 9
        d = nd
        r, c = nx, ny
        count += 1
    # b
    else:
        d = nd
        turn_count += 1
        if turn_count == 4:
            nd = (d + 2) % 4
            nx, ny = r + dx[nd], c + dy[nd]
            # d
            if graph[nx][ny] == 1:
                Continue = False
                break
            # c
            else:
                turn_count = 0
                r, c = nx, ny

print(count)