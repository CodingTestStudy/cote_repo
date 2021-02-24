import sys
sys.setrecursionlimit(10**5) # dfs방식을 사용하여 재귀가 많이 발생하기 때문에, 수동으로 재귀 횟수 설정
N, M = map(int, sys.stdin.readline().strip().split())
ice = [] # 빙산 위치 저장 리스트
data = [] # 데이터 입력받는 리스트
for i in range(N):
    x = list(map(int, sys.stdin.readline().strip().split()))
    data.append(x)
    for j in range(M):
        if x[j] > 0: # 빙산 발견시
            ice.append((i, j))

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1년 후 빙하
def task(visited):
    # 각 빙산의 높이가 감소되어야 하더라도 한꺼번에 감소 연산을 해야한다.
    # 감소 조건이 충족될 때마다 바로바로 감소연산을 해버리면, 그 뒤에 조건이 충족하는 빙산들이
    # 연쇄적으로 영향을 받기 때문
    calc_list = [] # 감소 연산을 한번에 하기위해, 빙산 위치와 높이 감소량을 저장하는 리스트
    for r, c in ice:
        minus_value = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if data[nr][nc] == 0: # 주변 위치 값이 0, 즉 바다라면
                minus_value -= 1 # 감소량 축적
        calc_list.append((r, c, minus_value)) # 해당 위치와 그에 해당하는 감소량 같이 저장

    del_list = [] # 바다가 되어 삭제될 빙산 index를 저장할 리스트
    # 연산 리스트 calc_list에 저장된 값들 토대로 연산
    for k in range(len(calc_list)):
        r, c, minus_value = calc_list[k]
        data[r][c] += minus_value # 해당 위치의 빙산 감소량만큼 감소
        if data[r][c] <= 0: # 바다가 되었다면
            data[r][c] = 0 # 바다값으로 갱신 후
            del_list.append(k) # 해당 index를 삭제 리스트에 저장
        else:
            visited[r][c] = True # 남은 빙산 위치는 방문 처리, dfs함수에서 빙산 덩어리 확인할 때 쓰임

    # 빙산에서 바다가된 index들 ice리스트에서 삭제
    # 리스트에서 앞의 index가 삭제되면 그 뒤의 index들이 앞으로 밀리기 때문에 x 변수로 index 위치 조정
    x = 0
    for value in del_list:
        del ice[value + x]
        x -= 1


# 빙하 덩어리 개수 확인
def dfs(r, c, visited):
    if not(0 <= r < N) or not(0 <= c < M): # 범위를 벗어난 경우
        return False
    if visited[r][c]: # 빙산을 만난 경우
        visited[r][c] = False # 방문처리 취소 후
        # 해당 위치를 기준을 상하좌우로 dfs함수 재귀
        dfs(r - 1, c, visited)
        dfs(r, c - 1, visited)
        dfs(r + 1, c, visited)
        dfs(r, c + 1, visited)
        return True
    return False

time = 0 # 빙산이 분리되는 시간 변수
result = 0 # 빙산의 상태 변수
while result <= 1: # 빙산이 분리될 때까지 반복
    visited = [[False] * M for _ in range(N)] # 빙산 방문 여부 초기화
    task(visited) # 1년 후의 빙산 상태 갱신 함수
    result = 0
    sum_value = 0 # 모든 빙산의 높이를 합한 값
    for i in range(1, N):
        for j in range(1, M):
            sum_value += data[i][j] # 모든 빙산의 높이 합
            if dfs(i, j, visited):
                result += 1 # 빙산 덩어리 개수 증가
    time += 1
    if sum_value == 0: # 전부 바다인 경우
        time = 0
        break
print(time)
