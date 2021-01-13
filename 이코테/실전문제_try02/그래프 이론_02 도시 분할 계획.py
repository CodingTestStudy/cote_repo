# 도시 분할 계획
# n : 도시 개수 (2 <= n <= 100,000)
# m : 길의 개수 (1 <= m <= 1,000,000)
# a -> b : c원 (1 <= c <= 1,000))
import sys

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

input = sys.stdin.readline
n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []
result = []

for i in range(1, n + 1):
  parent[i] = i

for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()

for e in edges:
  cost, a, b = e
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result.append(cost)
    print(cost)

print(sum(result) - result[len(result) - 1])