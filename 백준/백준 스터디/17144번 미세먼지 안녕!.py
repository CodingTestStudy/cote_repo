import sys
R, C, T = map(int, sys.stdin.readline().strip().split())
A = [[] for _ in range(R)]
dust = set()
air_cleaner = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(R):
    A[i] = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(C):
        if A[i][j] == -1:
            air_cleaner.append((i, j)) # 공기 청정기 위치 저장
        if A[i][j] != -1 and A[i][j] != 0:
            dust.add((i, j)) # 미세먼지 위치 저장

# 각각 공기 청정기 위치
air2 = air_cleaner.pop()
air1 = air_cleaner.pop()

while T != 0: # T초 동안
    T -= 1
    ##### 미세먼지 확산 #####

    new_dust = set() # 확산된 미세먼지 위치 저장할 set
    temp = [] # 확산을 유발한 미세먼지 위치 저장
    for value in dust:
        r, c = value
        count = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not(0 <= nr < R) or not(0 <= nc < C): continue # 범위 벗어남
            if A[nr][nc] == -1: continue # 공기 청정기 만남
            if A[r][c] // 5 > 0: # 미세먼지 확산이 가능하다면
                new_dust.add((nr, nc)) # 해당 위치 저장
                temp.append((nr, nc, A[r][c] // 5))
            count += 1
        if count > 0: # 확산이 존재한다면
            temp.append((r, c, -(A[r][c] // 5) * count))

    # 확산 유발 미세먼지 값 갱신
    for value in temp:
        r, c, x = value
        A[r][c] += x
    # 확산된 미세먼지 값 갱신
    for value in new_dust:
        r, c = value
        dust.add((r, c))

    ##### 공기청정기 #####

    # 미세먼지 리스트 복사
    # 바람 방향대로 값을 갱신하면 똑같은 값이 계속 복사되기 때문
    temp_A = [x[:] for x in A]
    row1, col1 = air1 # 위의 공기 청정기
    row2, col2 = air2 # 아래의 공기 청정기

    # 바람 방향대로 순환
    while True: # 왼쪽에서 오른쪽으로(공기청정기1,2 공통)
        if col1 + 1 == C: break
        A[row1][col1 + 1] = temp_A[row1][col1]
        A[row2][col2 + 1] = temp_A[row2][col2]
        dust.add((row1, col1 + 1))
        dust.add((row2, col2 + 1))
        col1 += 1
        col2 += 1
    A[air1[0]][air1[1] + 1] = 0
    A[air2[0]][air2[1] + 1] = 0
    while True: # 아래에서 위로(공기청정기1)
        if row1 - 1 == -1: break
        A[row1 - 1][col1] = temp_A[row1][col1]
        dust.add((row1 - 1, col1))
        row1 -= 1
    while True: # 위에서 아래로(공기청정기2)
        if row2 + 1 == R: break
        A[row2 + 1][col2] = temp_A[row2][col2]
        dust.add((row2 + 1, col2))
        row2 += 1
    while True: # 왼쪽에서 오른쪽(공기청정기1,2 공통)
        if col1 - 1 == -1: break
        A[row1][col1 - 1] = temp_A[row1][col1]
        A[row2][col2 - 1] = temp_A[row2][col2]
        dust.add((row1, col1 - 1))
        dust.add((row2, col2 - 1))
        col1 -= 1
        col2 -= 1
    while True: # 위에서 아래로(공기청정기1)
        if row1 + 1 == air1[0]: break
        A[row1 + 1][col1] = temp_A[row1][col1]
        dust.add((row1 + 1, col1))
        row1 += 1
    while True: # 아래에서 위로(공기청정기2)
        if row2 - 1 == air2[0]: break
        A[row2 - 1][col2] = temp_A[row2][col2]
        dust.add((row2 - 1, col2))
        row2 -= 1


count = 0
for i in range(R):
    count += sum(A[i])
print(count + 2)