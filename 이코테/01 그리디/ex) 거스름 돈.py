money = 1260
count = 0
# 큰 단위의 화폐부터 차례대로 확인하기
# 큰 단위가 항상 작은 단위의 배수인 경우에만 가능한 솔루션
coin_list = [500, 100, 50, 10]
 
for coin in coin_list:
  count += money // coin # 해당 화폐로 거술러 줄 수 있는 동전의 개수 세기
  money %= coin


print(count)
