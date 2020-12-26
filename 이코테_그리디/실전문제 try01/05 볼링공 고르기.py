# 볼링공 고르기
# 입력 : 5 3 (볼링공 개수, 무게 max값)
# 입력 : 1 3 2 3 2 (볼링공 무게들)
# 출력 : 8

# 입력 : 8 5
# 입력 : 1 5 4 3 2 4 5 2
# 출력 : 25

n, m = map(int, input().split())
ball = list(map(int, input().split()))
count = 0
ball.sort() # 오름차순으로 정렬
# i는 주체가 되는 공
# j는 비교대상 -> j는 처음 시작할 때 i 보다 1 큰 상태(다음 공)로 시작
for i in range(0, n - 1):
  for j in range(i + 1, n):
    # 다음 공과 비교했을 때, 무게가 다르면 남은 공 개수만큼 count   
    # 무게가 같으면, 같은 무게를 들 수 없으니, 다음 공(j+1)과 다시 비교
    if ball[i] != ball[j]: 
      count += n - j      
      break

print(count)
    