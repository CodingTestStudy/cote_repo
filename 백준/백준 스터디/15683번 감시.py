import sys
N, M = map(int, sys.stdin.readline().strip().split())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
min_count = 1e9

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
d = [0,
     [[0], [1], [2], [3]], # 1번
     [[0, 1], [2, 3]], # 2번
     [[1, 2], [1, 3], [0, 2], [0, 3]], # 3번
     [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번
     [[0, 1, 2, 3]] # 5번
     ]


def dfs(start, data, cctv):
    global min_count
    if start == len(cctv): # 모든 cctv를 확인했을 경우
        cnt = 0
        # 사각지대의 개수를 확인
        for r in range(N):
            for c in range(M):
                if data[r][c] == 0:
                    cnt += 1
        # 사각지대의 개수의 최소값들을 구함
        # 재귀함수로 반복되기 때문에, 모든 재귀함수가 마무리 될 시점에는
        # 최종 최소 cnt값이 min_count에 남는다.
        min_count = min(min_count, cnt)
        return

    num, r, c = cctv[start] # start번째 cctv에 대해서
    for dir in d[num]: # cctv 번호에 해당하는 이동 가능 범위
        temp = [x[:] for x in data] # 기존의 입력 받은 data 복사
        for i in dir:
            nr, nc = r + dr[i], c + dc[i]
            while 0 <= nr < N and 0 <= nc < M:
                if temp[nr][nc] == 6: break # 이동 좌표가 벽인 경우 break
                elif temp[nr][nc] == 0:
                    temp[nr][nc] = '#'
                nr += dr[i]
                nc += dc[i]
        # 31번째줄 for문 안에 존재하기 때문에, 이동 가능 범위들의 모든 경우들에 대해 재귀
        dfs(start + 1, temp, cctv) # 다음 cctv index와 변경된 데이터 리스트와 함께 재귀


cctv = [] # cctv 번호, 좌표 저장 리스트
for r in range(N):
    for c in range(M):
        if data[r][c] not in [0, 6]: # 좌표 값이 1~5이면
            cctv.append([data[r][c], r, c]) # cctv 리스트에 저장
dfs(0, data, cctv)
print(min_count)