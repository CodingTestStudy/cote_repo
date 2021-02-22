import sys
sys.setrecursionlimit(10**5)
N, M = map(int, sys.stdin.readline().strip().split())
ice = []
data = []
for i in range(N):
    x = list(map(int, sys.stdin.readline().strip().split()))
    data.append(x)
    for j in range(M):
        if x[j] > 0: ice.append((i, j))

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1년 후 빙하
def task(visited):
    calc_list = []
    for r, c in ice:
        minus_value = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if data[nr][nc] == 0:
                if data[r][c] == 0: break
                else: minus_value -= 1
        calc_list.append((r, c, minus_value))

    del_list = []
    for k in range(len(calc_list)):
        r, c, minus_value = calc_list[k]
        data[r][c] += minus_value
        if data[r][c] <= 0:
            data[r][c] = 0
            del_list.append(k)
        else:
            visited[r][c] = True

    index = 0
    for value in del_list:
        del ice[value + index]
        index -= 1


# 빙하 덩어리 개수 확인
def dfs(r, c, visited):
    if not(0 <= r < N) or not(0 <= c < M): return False
    if visited[r][c]:
        visited[r][c] = False
        dfs(r - 1, c, visited)
        dfs(r, c - 1, visited)
        dfs(r + 1, c, visited)
        dfs(r, c + 1, visited)
        return True
    return False

time = 0
result = 0
while result <= 1:
    visited = [[False] * M for _ in range(N)]
    task(visited)
    result = 0
    sum_value = 0
    for i in range(1, N):
        for j in range(1, M):
            sum_value += data[i][j]
            if dfs(i, j, visited):
                result += 1
    time += 1
    if sum_value == 0:
        time = 0
        break
print(time)
