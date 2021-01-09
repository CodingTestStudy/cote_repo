# 계수 정렬
d = [0] * 1000001
n = int(input())
for i in input().split():
  d[int(i)] = 1

m = int(input())
m_array = list(map(int, input().split()))

for i in m_array:
  if d[i] == 1:
    print("yes")
  else:
    print("no")

