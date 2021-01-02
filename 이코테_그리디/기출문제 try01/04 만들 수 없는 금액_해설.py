# 만들 수 없는 금액
# 입력 : 5 (동전의 개수)
# 입력 : 3 2 1 1 9 (화폐 단위들)
# 출력 : 8 (화폐 단위들로 만들 수 없는 최솟값)

n = int(input())  # 동전 개수 입력
coin = list(map(int, input().split())) # 화폐 단위들 
coin.sort() # 오름차순
# 어차피 최솟값을 구하는 것이기 때문에, 전체 경우의 수 구할 필요 x
# 오름차순에서 값을 더해나가는 것이 
# n개를 더했을 때의 최솟값들이다.
# coin들 중에 가장 작은 값이 1이 아닌 경우엔 이전에 target = 1인 상태에서
# 덧셈을 시작하기 때문에, 최솟값에 1을 더할 필요 없다. 이미 더해져있는 상태

target = 1
for x in coin:
  if target < x: break
  target += x

print(target)
