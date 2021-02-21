import sys

q = [] # 아기 상어 경로 리스트
N = int(sys.stdin.readline().strip())
visited = [[False] * N for _ in range(N)] # 상어의 방문여부 초기화
space = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
for i in range(N):
    flag = False
    for j in range(N):
        if space[i][j] == 9:
            q = [[i, j]] # 아기 상어 위치 삽입
            space[i][j] = 0 # 아기 상어자리 0으로 초기화
            visited[i][j] = True # 아기 상어 방문 처리
            flag = True
            break
    if flag: # 아기 상어 찾았으면 반복문 종료
        break

# 아기 상어의 상태를 확인하고, 할당량을 모두 먹어서 0이 되었을 경우,
# 상어의 크기와 상어가 먹을 수 있는 할당량을 상어의 크기로 재할당 해주는 함수
def level_up():
    global shark_size, shark_eat
    if shark_eat == 0:
        shark_size += 1
        shark_eat = shark_size
    return


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
distance = 0 # 아기 상어가 먹이를 발견할 때까지의 거리
result = 0 # 최종 걸린 시간
shark_size, shark_eat = 2, 2 # 아기상어 크기와 할당량 초기화
while q: # 아기 상어가 갈 곳이 없을 때까지 반복
    distance += 1 # 한칸 이동
    eaten = [] # 먹이 리스트 초기화
    for _ in range(len(q)):
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 해당 좌표가 범위를 벗어났으면 무시
            if not(0 <= nr < N) or not(0 <= nc < N): continue
            # 해당 좌표의 물고기가 아기 상어보다 크면 무시
            if space[nr][nc] > shark_size: continue
            # 이전에 방문한적있는 좌표면 무시
            if visited[nr][nc]: continue
            # 해당 좌표의 물고기를 먹을 수 있는 경우
            if 0 < space[nr][nc] < shark_size:
                visited[nr][nc] = True # 방문 처리
                eaten.append([nr, nc]) # 먹이 리스트에 저장
            # 자기와 크기가 같거나, 물고기가 없는 경우 (그냥 지나갈 수 있는 경우)
            if space[nr][nc] == shark_size or space[nr][nc] == 0:
                visited[nr][nc] = True # 방문 처리
                q.append([nr, nc]) # 경로 리스트에 저장

    # 지나다니면서 먹이가 존재했을 경우
    # 물고기가 여럿 있을 경우, 문제의 조건에 맞춰 선정해야 함
    if eaten:
        er, ec = N - 1, N - 1
        for e in eaten:
            # 가장 위의 물고기 찾기
            if e[0] < er:
                er, ec = e[0], e[1]
            # 가장 위 물고기가 여럿 있다면 가장 왼쪽 물고기 찾기
            elif e[0] == er:
                if e[1] < ec:
                    ec = e[1]

        shark_eat -= 1 # 한마리 먹음, 할당량 감소
        level_up() # 아기 상어 상태 확인
        q = [[er, ec]] # 현재 먹이 먹은 좌표를 경로 리스트에 저장
        result += distance # 촤종 거리에 지금까지 돌아다닌 거리 추가
        distance = 0 # 거리 초기화
        space[er][ec] = 0 # 현재 위치 먹이 먹었으므로 0으로 초기화
        visited = [[False] * N for _ in range(N)] # 방문 여부 초기화
        visited[er][ec] = True # 현재 위치는 방문 처리
print(result)
