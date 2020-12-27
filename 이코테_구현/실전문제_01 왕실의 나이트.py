# 왕실의 나이트
# 입력 : c2
# 출력 : 6
import time

n = input()
start = time.time()
count = 0
# 입력받은 값들을 각 좌표값으로 변환
x = int(n[1]) 
y = ord(n[0]) - 96
knite = [x, y]  # 나이트의 위치

# 나이트의 위치에서 이동할 수 있는 단위
calc = [[-2, 1], [-1, -2], [-2, 1], [-1, 2], [2, -1], [1, -2], [2, 1], [1, 2] ]
for i in range(len(calc)):  
  # nite의 위치가 범위를 벗어나지 않았을 경우, count 증가  
  if 0 < knite[0] + calc[i][0] <= 8 and 0 < knite[1] + calc[i][1] <= 8:     
    count += 1     
    
print(count)
print(time.time() - start)
  





