import sys

# 미세먼지 확산
def dust_diffusion():
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우
    temp = [[0] * C for _ in range(R)] # home 크기의 임시 저장 리스트, 미세먼지 확산값 한번에 연산위해
    dif_dust = 0 # 미세먼지 확산량 변수 선언
    for r in range(R):
        for c in range(C):
            if home[r][c] > 0: # 미세먼지가 존재한다면
                cnt = 0 # 확산 위치 개수 변수 선언
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    # 이동 위치가 범위에 만족하고 공기 청정기가 아니라면
                    if 0 <= nr < R and 0 <= nc < C and home[nr][nc] != -1:
                        dif_dust = home[r][c] // 5 # 해당 위치에서의 미세먼지 확산량 저장
                        temp[nr][nc] += dif_dust # 임시 저장 리스트에 확산량 축적
                        cnt += 1 # 확산 위치 개수 증가

                # 해당위치 미세먼지값에 (확산량 x 확산 위치 개수) 만큼 감소
                home[r][c] -= dif_dust * cnt

    for r in range(R):
        for c in range(C):
            # 확산된 위치에 해당하는 부분을 임시 저장 리스트에 저장된 값을 통해 갱신
            if temp[r][c] > 0:
                home[r][c] += temp[r][c]


# 공기 청정기 작동
def air_cleaner():
    for i in range(2): # 각 공기청정기 기준으로 위, 아래 나눠서 연산
        cr, cc = machine[i][0], machine[i][1] # 공기 청정기 위치
        rotate = 0 # 공기 순환 방향

        # 공기청정기 바람 방향으로 반복문을 진행할 경우
        # 순차적으로 데이터값을 옮길 시, 데이터를 미리 복사해두고 할당하지 않는다면
        # 이전의 똑같은 데이터값들이 계속 할당될 것이기 때문에,
        # 바람의 반대방향으로 할당해주는 식으로 진행
        if i == 0:
            cr -= 1
            # 시계방향
            dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
            while rotate != 4: # 한바퀴 도는동안
                nr = cr + dr[rotate]
                nc = cc + dc[rotate]
                if 0 <= nr <= machine[i][0] and 0 <= nc < C:
                    if home[nr][nc] != -1: # 이동 좌표가 공기청정기가 아니라면
                        home[cr][cc] = home[nr][nc] # 값 이동
                    else: # 이동좌표가 공기 청정기라면
                        home[cr][cc] = 0
                    cr, cc = nr, nc
                else: # 범위 벗어나면 방향 전환
                    rotate += 1

        else:
            cr += 1
            # 반시계방향
            dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
            while rotate != 4:
                nr = cr + dr[rotate]
                nc = cc + dc[rotate]
                if machine[i][0] <= nr < R and 0 <= nc < C:
                    if home[nr][nc] != -1:
                        home[cr][cc] = home[nr][nc]
                    else:
                        home[cr][cc] = 0
                    cr, cc = nr, nc
                else:
                    rotate += 1


R, C, T = map(int, sys.stdin.readline().strip().split())
home = []
machine = [] # 공기청정기 위치 저장 리스트
for i in range(R):
    x = list(map(int, sys.stdin.readline().strip().split()))
    home.append(x)
    for j in range(C):
        if x[j] == -1:
            machine.append((i, j)) # 공기청정기 위치 저장


# T초 만큼 반복
for _ in range(T):
    dust_diffusion() # 미세먼지 확산
    air_cleaner() # 공기청정기 작동

# 최종적으로 저장된 미세먼지 값들 모두 더함
result = 0
for i in home:
    result += sum(i)

# 공기 청정기 -1이 2개 더해졌기 때문에, result + 2로 출력
print(result + 2)