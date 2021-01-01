# 적절한 높이를 찾을 때까지 이진탐색을 수행하여 높이 h를 반복해서 조정
# 절단기 높이 0~10억까지의 정수 중 하나
# -> 이렇게 큰 탐색 범위를 보면 가장 먼저 '이진 탐색'을 떠올려야함

n, m = map(int, input().split())
dduk = list(map(int, input().split()))
x = 0
h = 0
while True:  
  for i in dduk:    
    if i >= h:
      x += i - h
  
  if x >= m:        
    h += 1
    x = 0
  else:
    h -= 1
    break

print(h)