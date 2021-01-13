# 효율적인 화폐 구성
# n : 화폐 종류 개수 (1 <= n <= 100)
# m : 가치의 합 (1 <= m <= 10,000)

# n ,m = map(int, input().split())
# money = []
# d = [100001] * 10000
# for _ in range(n):
#   money.append(int(input()))

# for i in money:
#   d[i] = 1

# for i in range(1, m + 1):  
#   for value in money:
#     if i % value == 0:
#       d[i] = min(d[i], d[i - value] + 1)      

# if d[m] == 100001:
#   print(-1)
# else:  
#   print(d[m])
    

n, m = map(int, input().split())
array = []
for i in range(n):
  array.append(int(input()))

d = [100001] * (m + 1)
d[0] = 0
for i in range(n):
  for j in range(array[i], m + 1):
    if d[j - array[i]] != 100001:
      d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 100001:
  print(-1)
else:
  print(d[m])
  


