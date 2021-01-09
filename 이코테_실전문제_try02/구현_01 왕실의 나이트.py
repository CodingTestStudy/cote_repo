# 왕실의 나이트
# 8 X 8 좌표에서 나이트가 이동할 수 있는 경우의 수 출력
# a1(입력), 2(출력)
data = input()
x = ord(data[0]) - ord('a') + 1
y = int(data[1])
count = 0
location = [
  (x - 2, y - 1), (x - 1, y - 2), 
  (x + 2, y - 1), (x + 1, y - 2), 
  (x - 2, y + 1), (x - 1, y + 2), 
  (x + 2, y + 1), (x + 1, y + 2)
]

for loc in location:
  if 1 <= loc[0] <= 8 and 1 <= loc[1] <= 8:    
    count += 1
print(count)