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
            air_cleaner.append((i, j))
        if A[i][j] != -1 and A[i][j] != 0:
            dust.add((i, j))
air2 = air_cleaner.pop()
air1 = air_cleaner.pop()

while T != 0:
    T -= 1
    new_dust = set()
    temp = []
    for value in dust:
        r, c = value
        count = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not(0 <= nr < R) or not(0 <= nc < C): continue
            if A[nr][nc] == -1: continue
            if A[r][c] // 5 > 0:
                new_dust.add((nr, nc))
                temp.append((nr, nc, A[r][c] // 5))
            count += 1
        if count > 0:
            temp.append((r, c, -(A[r][c] // 5) * count))

    for value in temp:
        r, c, x = value
        A[r][c] += x

    for value in new_dust:
        r, c = value
        dust.add((r, c))

    temp_A = [x[:] for x in A]
    row1, col1 = air1
    row2, col2 = air2
    while True:
        if col1 + 1 == C: break
        A[row1][col1 + 1] = temp_A[row1][col1]
        A[row2][col2 + 1] = temp_A[row2][col2]
        dust.add((row1, col1 + 1))
        dust.add((row2, col2 + 1))
        col1 += 1
        col2 += 1
    A[air1[0]][air1[1] + 1] = 0
    A[air2[0]][air2[1] + 1] = 0
    while True:
        if row1 - 1 == -1: break
        A[row1 - 1][col1] = temp_A[row1][col1]
        dust.add((row1 - 1, col1))
        row1 -= 1
    while True:
        if row2 + 1 == R: break
        A[row2 + 1][col2] = temp_A[row2][col2]
        dust.add((row2 + 1, col2))
        row2 += 1
    while True:
        if col1 - 1 == -1: break
        A[row1][col1 - 1] = temp_A[row1][col1]
        A[row2][col2 - 1] = temp_A[row2][col2]
        dust.add((row1, col1 - 1))
        dust.add((row2, col2 - 1))
        col1 -= 1
        col2 -= 1
    while True:
        if row1 + 1 == air1[0]: break
        A[row1 + 1][col1] = temp_A[row1][col1]
        dust.add((row1 + 1, col1))
        row1 += 1
    while True:
        if row2 - 1 == air2[0]: break
        A[row2 - 1][col2] = temp_A[row2][col2]
        dust.add((row2 - 1, col2))
        row2 -= 1


count = 0
for i in range(R):
    count += sum(A[i])
print(count + 2)