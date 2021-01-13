# 피보나치 수열
# 탑다운 다이나믹 프로그래밍
# 재귀 함수 사용

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
  # 종료 조건(1 혹은 2일 때 1을 반환)
  if x == 1 or x == 2:
    return 1
  # 이미 계산한 적 있는 문제라면 그대로 반환
  if d[x] != 0:
    return d[x]  
  d[x] = fibo(x - 2) + fibo(x - 1)
  return d[x]

print(fibo(99))