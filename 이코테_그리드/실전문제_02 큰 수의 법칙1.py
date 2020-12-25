# n : 배열크기, m : 총 m번의 덧셈, k : 중복 덧셈 최대 횟수
n, m, k = map(int, input().split())
number = list(map(int, input().split()))
number.sort(reverse=True) # 내림차순 정렬
a = number[0] # 가장 큰 수
b = number[1] # 그 다음 큰 수

result = 0  

while True:
  for _ in range(k):  # 홀수 번째에는 가장 큰 값 k번 덧셈
    if m == 0: break  # 더할 수 있는 기회가 없는 경우 
    result += a 
    m -= 1  # 덧셈 가능한 횟수 1씩 감소
  
  if m == 0: break  # 더할 수 있는 기회가 없는 경우 
  else: # 짝수 번째에는 두번째로 큰 값 최소한으로 (1번) 덧셈
    result += b
    m -= 1 # 덧셈 가능한 횟수 1씩 감소
  
print(result)