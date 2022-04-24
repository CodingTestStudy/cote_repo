import sys
from copy import deepcopy
sys.setrecursionlimit(100000)

input = sys.stdin.readline
n = int(input())
grid = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for _ in range(n):
    grid.append(list(input().strip()))


def dfs(r, c, color, temp):
    # 범위 이탈
    if r < 0 or c < 0 or r >= n or c >= n:
        return False
    if temp[r][c] in color:
        temp[r][c] = 'X'
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            dfs(nr, nc, color, temp)
        return True
    return False


blue_cnt, green_cnt, red_cnt, green_red_cnt = 0, 0, 0, 0
grid1, grid2, grid3, grid4 = deepcopy(grid), deepcopy(grid), deepcopy(grid), deepcopy(grid)

for i in range(n):
    for j in range(n):
        if dfs(i, j, 'B', grid1):
            blue_cnt += 1
for i in range(n):
    for j in range(n):
        if dfs(i, j, 'G', grid2):
            green_cnt += 1
for i in range(n):
    for j in range(n):
        if dfs(i, j, 'R', grid3):
            red_cnt += 1
for i in range(n):
    for j in range(n):
        if dfs(i, j, 'GR', grid4):
            green_red_cnt += 1

print(blue_cnt + green_cnt + red_cnt, end=' ')
print(blue_cnt + green_red_cnt)

