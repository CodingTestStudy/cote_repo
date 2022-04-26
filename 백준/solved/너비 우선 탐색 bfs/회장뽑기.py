import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [[1e9] * (n + 1) for _ in range(n + 1)]

while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    graph[x][y] = 1
    graph[y][x] = 1

# 자기 자신 경로
for i in range(1, n + 1):
    graph[i][i] = 0

# 플로이드 와샬
for k in range(1, n + 1):
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            # 직접 연결되어 있거나 자기 자신인 경우 -> 제외
            if graph[r][c] == 1 or graph[r][c] == 0:
                continue
            if graph[r][c] > graph[r][k] + graph[k][c]:
                graph[r][c] = graph[r][k] + graph[k][c]

candidate = []
for i in range(1, n + 1):
    candidate.append(max(graph[i][1:]))

min_value = min(candidate)
answer_list = []
for i in range(n):
    if candidate[i] == min_value:
        answer_list.append(i + 1)
print(min_value, len(answer_list))
print(*answer_list)