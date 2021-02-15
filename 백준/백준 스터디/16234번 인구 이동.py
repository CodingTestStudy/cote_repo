import sys
from collections import deque

N, L, R = map(int, input().split())
nation = deque()
united = deque()
# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for r in range(N):
    nation.append(list(map(int, sys.stdin.readline().strip().split())))


# 현재 위치에서 인구 이동이 가능하면 인구 이동을 하는 함수
def bfs(row, column, visited, nation, united):
    if visited[row][column]: return False # 시작지점이 이전에 다룬 지역이면 pass
    visited[row][column] = True # 시작지점 방문 처리
    united.append((row, column)) # 시작지점 삽입, 연합 리스트2 (너비 우선 탐색을 하기 위한 리스트)
    united_list = []  # 연합 리스트1 (평균값 계산하기 위해 별도로 만듬)
    united_list.append((row, column)) # 시작지점 삽입
    while united: # 연합이 없을 때까지
        r, c = united.popleft() # 현재 연합내의 나라 좌표에 대해서 다룸
        for i in range(4):  # 상하좌우
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 벗어나면 무시
            if not (0 <= nr < N) or not (0 <= nc < N): continue
            # 이전에 방문한 적 있는 나라라면 무시
            if visited[nr][nc]: continue
            # 이웃한 나라와의 인구차이가 L,R 사이라면
            if L <= abs(nation[nr][nc] - nation[r][c]) <= R:
                visited[nr][nc] = True # 방문 처리
                united.append((nr, nc)) # 해당 나라 삽입
                united_list.append((nr, nc)) # 해당 나라 삽입

    if len(united_list) > 1: # 연합이 존재한다면 (시작 지점은 무조건 들어가기 때문에 1보다 커야함)
        sum_value = 0
        for rr, cc in united_list:
            sum_value += nation[rr][cc]
        avr = sum_value // len(united_list) # 평균값

        # 연합에 속하는 나라 인구 수 평균값으로 수정
        for rr, cc in united_list:
            nation[rr][cc] = avr
        return True
    else: # 연합이 존재하지 않는다면면
       return False


count = 0 # 인구 이동 횟수
Continue = True
while Continue:
    visited = [[False] * N for _ in range(N)] # 나라 방문 여부 초기화
    temp = [data[:] for data in nation] # 나라 데이터 복사
    for i in range(N):
        for j in range(N):
            # 현재 나라 상태에서 인구 변화시키는 함수
            # 모든 구역에서 검사 시작해봄
            # 너비 우선 탐색인데, 처음부터 끝나는 경우가 생길 수 있기 때문에
            x = bfs(i, j, visited, temp, united)

    flag = False # 나라 인구 변화가 있는지 확인할 bool변수

    # 인구 변화가 있는지 반복문으로 확인, 다른 방법이 있으면 좋을 듯
    for i in range(N):
        for j in range(N):
            # 인구 변화를 발견했다면
            if nation[i][j] != temp[i][j]:
                count += 1 # 인구 이동 횟수 증가
                flag = True # 인구 변화 했음을 저장
                break
        if flag: # 인구 변화했기 때문에 더이상 반복문 X
            break

    # 변화가 없었다면, while문 벗어남
    if not flag:
        Continue = False

    # 다음 bfs를 위해, 현재 변화한 상태로 nation 초기화
    nation = [data[:] for data in temp]

print(count)