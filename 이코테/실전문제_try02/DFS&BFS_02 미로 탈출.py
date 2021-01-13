# 미로 탈출 (N x M)
# 현재 위치 (1, 1)
# 출구 (n, m)
# 0 : 괴물, 1 : 괴물 x
# 4 <= n, m <= 200
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

print(graph)

x = 0
y = 0
graph[x][y] = 1
direction = [(0, 1), (1, 0)]

def bfs(x, y):  
  for d in direction:
    while 0 <= x + d[0] < n and 0 <= y + d[1] < m:
      if graph[x + d[0]][y + d[1]] == 1:        
        graph[x + d[0]][y + d[1]] = graph[x][y] + 1
        print(graph)
        bfs(x + d[0], y + d[1])
      else:
        break

bfs(0, 0)
print(graph[n - 1][m - 1])
direction = [(0, 1), (1, 0)]

def bfs(x, y):  
  for d in direction:
    while 0 <= x + d[0] < n and 0 <= y + d[1] < m:
      if graph[x + d[0]][y + d[1]] == 1:        
        graph[x + d[0]][y + d[1]] = graph[x][y] + 1
        print(graph)
        bfs(x + d[0], y + d[1])
      else:
        break

bfs(0, 0)
print(graph[n - 1][m - 1])
direction = [(0, 1), (1, 0)]

def bfs(x, y):  
  for d in direction:
    while 0 <= x + d[0] < n and 0 <= y + d[1] < m:
      if graph[x + d[0]][y + d[1]] == 1:        
        graph[x + d[0]][y + d[1]] = graph[x][y] + 1
        print(graph)
        bfs(x + d[0], y + d[1])
      else:
        break

bfs(0, 0)
print(graph[n - 1][m - 1])