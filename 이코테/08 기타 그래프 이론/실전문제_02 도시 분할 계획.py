# 크루스칼 알고리즘
# edges, result 사용

#-------------------------------------
#                 오답
#        2개로 분할하지 못했다.
#-------------------------------------
n, m = map(int, input().split())
city = [0] * (n + 1)
edges = []
result = 0
for i in range(1, n + 1):
  city[i] = i

def find_city(city, x):
  if city[x] != x:
    city[x] = find_city(city, city[x])
  return city[x]

def union_city(city, a, b):
  a = find_city(city, a)
  b = find_city(city, b)
  if a < b:
    city[b] = a
  else:
    city[a] = b

for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))

edges.sort()

for e in edges:
  cost, a, b = e
  if find_city(city, a) != find_city(city, b):
    union_city(city, a, b)
    result += cost

print(result)
