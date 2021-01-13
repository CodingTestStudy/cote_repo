# # 음료수 얼려 먹기
def dfs(x, y):
  if not(0 <= x < n and 0 <= y < m):
    return False
  
  # 해당 좌표가 1 즉, 방문된 곳이라면, False를 return해서 아래 for문에서 result += 1 처리 안된다.
  if graph[x][y] == 0:
    graph[x][y] = 1 # 방문 처리
    # 상하좌우 이동
    # 이동하면서 0인 부분 1로 바꾸는 역할
    # 1을 만나면 return False
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  return False


n, m = map(int, input().split())
result = 0
graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)

