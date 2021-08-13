N, M = map(int, input().split())
marble = []
for _ in range(M):
    x, y = map(int, input().split())
    marble.append([x, y])

total = [['?' for _ in range(N)] for _ in range(N)]

for i in range(N):
    total[i][i] = 'SELF'

for result in marble:
    total[result[0] - 1][result[1] - 1] = 'HEAVY'
    total[result[1] - 1][result[0] - 1] = 'LIGHT'

for k in range(N):
    for i in range(N):
        for j in range(N):
            if total[i][k] == 'HEAVY' and total[k][j] == 'HEAVY':
                total[i][j] = 'HEAVY'
            elif total[i][k] == 'LIGHT' and total[k][j] == 'LIGHT':
                total[i][j] = 'LIGHT'

answer = 0
mid = int((N + 1) / 2)
for i in range(N):
    h = total[i].count('HEAVY')
    l = total[i].count('LIGHT')
    if h >= mid or l >= mid:
        answer += 1
print(answer)
