# 커리큘럼 (위상 정렬 알고리즘)
# n : 강의 수 (1 <= n <= 500)
# time , course ... -1
from collections import deque
import sys, copy
input = sys.stdin.readline
n = int(input())
indegree = [0] * (n + 1)
time = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
  input_data = list(map(int, input().split()))
  time[i] = input_data[0]
  for x in input_data[1 : -1]:
    graph[x].append(i)
    indegree[i] += 1

def topology_sort():
  result = copy.deepcopy(time)
  q = deque()

  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    now = q.popleft()
    for i in graph[now]:
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in range(1, n + 1):
    print(result[i])

topology_sort()
