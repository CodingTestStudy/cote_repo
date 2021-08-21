N = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for p in plans:
    for i in range(len(move)):
        if p == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny
print(x, y)