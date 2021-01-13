# 만들 수 없는 금액
# n : 동전의 개수 (1 <= n <= 1,000)
# m : 화폐단위 (1 <= m <= 1,000,000)

n = int(input())
m = list(map(int, input().split()))
m.sort()
value = 0
data = [] * 1000
while True:
  value += 1
  for i in m:
    data[value]

