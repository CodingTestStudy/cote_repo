# 효율적인 화폐 구성# 효울적인 화폐 구성
# ******************** 오답 ********************
# n, m = map(int, input().split())
# money = []
# d = [0] * 10000
# for i in range(n):
#   money.append(int(input()))
#   d[money[i]] = 1 # 입력받은 값의 개수를 1개로 지정

# money.sort(reverse=True)  # 가장 큰 화폐와 먼저 비교하기 위해 내림차순 

# for i in range(1, m + 1): # 1원부터 m원까지
#   for j in money: # 갖고 있는 화폐와 비교
#     k = i - j # j 화폐로 i원을 만들 수 있는가?
#     if k > 0 and d[k] > 0:  # k가 0보다 크고 이전에 k원을 만든 적이 있다면(만들 수 있다면),
#       d[i] = d[k] + 1 # i원은 k원을 만든 화폐 개수에 j원을 1회 추가      
#       break
#   # 갖고 있는 화폐로 만들 수 없는 경우
#   if d[i] == 0:
#     d[i] = -1

# print(d[m])

# ******************** 오답 ********************
  