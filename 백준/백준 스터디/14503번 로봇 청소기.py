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
count = 1 # 현재 위치 포함하기 때문에 1에서 시작
Continue = True
turn_count = 0 # 회전 횟수

while Continue:
    nd = (d + 3) % 4 # 왼쪽 회전
    nx, ny = r + dx[nd], c + dy[nd] # 왼쪽 회전 후, 한칸 이동한 임시 좌표
    # 2-a
    if graph[nx][ny] == 0: # 빈칸인 경우
        turn_count = 0 # 회전 횟수 초기화
        graph[nx][ny] = 9 # 청소처리
        d = nd # 방향 갱신
        r, c = nx, ny # 좌표 갱신
        count += 1 # 청소 칸 개수 증가
    # 2-b
    else: # 이미 청소를 한 칸이거나, 벽인 경우
        d = nd # 방향 갱신
        turn_count += 1 # 제자리 회전 횟수 증가
        if turn_count == 4: # 한바퀴를 돈 경우
            nd = (d + 2) % 4 # 후진 방향
            nx, ny = r + dx[nd], c + dy[nd] # 후진 좌표로 갱신
            # 2-d
            if graph[nx][ny] == 1: # 후진했는데 벽이라면
                Continue = False # 반복문 종료
                break
            # 2-c
            else: # 후진했는데 벽이 아닌 경우
                turn_count = 0 # 회전 횟수 초기화
                r, c = nx, ny # 현재 좌표 갱신
print(count)