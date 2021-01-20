from collections import deque

# bfs 사용
m, n = map(int, input().split())
tomato = []
first_tomato = []  # 초기에 토마토가 존재하는 위치를 담을 리스트
for i in range(n):
    input_data = list(map(int, input().split()))
    tomato.append(input_data)
    for j in range(m):
        if input_data[j] == 1:
            first_tomato.append((i, j))  # 초기 입력되는 토마토 위치 리스트에 저장

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
q = deque()


def bfs(start):  # 초기에 입력받은 토마토 위치가 저장된 리스트를 인자로 받음
    day = 1
    for f_r, f_c in start:  # 초기 토마토 위치 값들을 모두 큐에 삽입
        q.append((f_r, f_c))
    while q:    # 큐가 빌 때까지
        r, c = q.popleft()  # 큐에 있는 위치 값들을 pop으로 받고
        for i in range(4):  # 해당 위치를 기준으로 상하좌우 이동
            nr = r + dr[i]
            nc = c + dc[i]

            if not (0 <= nr < n and 0 <= nc < m): continue  # 이동한 위치가 범위를 벗어나면 무시
            if tomato[nr][nc] == -1 or tomato[nr][nc] > 1: continue  # 이동한 위치에 토마토가 존재하지 않거나, 이미 존재한다면 무시
            if tomato[nr][nc] == 0:  # 아직 익지 않은 토마토 위치라면
                tomato[nr][nc] = tomato[r][c] + 1   # 이전의 토마토가 익은 날짜보다 1일 증가
                day = max(tomato[nr][nc], day)  # 가장 오래된 날짜 저장
                q.append((nr, nc))  # 추가적으로 넓혀가기 위해, 해당 위치도 큐에 저장, 후에 while문을 통해 다시 pop되서 상하좌우 반복

    for value in tomato:    # 반복문을 마쳤음에도 익지 못한 토마토가 존재한다면
        if 0 in value:
            return -1   # -1 출력을 위해 -1 return

    return day - 1  # 초기 토마토 위치의 리스트 값이 1이기 때문에
    # 즉, 하루가 지나지 않았음에도 1부터 시작하였기 때문에, -1 연산 후 day return


print(bfs(first_tomato))
