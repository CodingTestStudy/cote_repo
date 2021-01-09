# 음료수 얼려 먹기
# 1 <= n, m <= 1,000
def dfs(x, y):
  if not(0 <= x < n and 0 <= y < m):
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  return False
    

n, m = map(int, input().split())
graph = []
result = 0
for _ in range(n):
  graph.append(list(map(int, input())))

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)