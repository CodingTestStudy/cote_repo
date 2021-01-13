# 커리큘럼
# 위성 정렬 알고리즘 사용
# 입력값 어떻게 설정해야 하는가? 2개, 3개 동시에 어떻게?
# 못품
from collections import deque

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

def topology_sort():
  result = []
  q = deque()
  time = 0
  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)  
  
  while q:
    now = q.popleft()
    result.append(now)
    time += now[0]
    print(timed)

    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i, end=' ')

n = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
  time, course, x = map(int, input().split())
  graph[i].append((time, course))
  indegree[course] += 1
  
topology_sort()