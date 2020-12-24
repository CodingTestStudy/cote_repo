# 93
n = int(input())
check = list(map(int, input().split()))
check_list = [int(0) for i in range(23)]

for i in range(10):
  for j in range(23):
    if check[i] == j: check_list[j - 1] += 1

print(check_list)
