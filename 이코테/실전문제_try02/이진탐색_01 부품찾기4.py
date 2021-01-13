# 집합 자료형
n = int(input())
n_array = set(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))

for i in m_array:
  if i in n_array:
    print("yes")
  else:
    print("no")