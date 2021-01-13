# 상하좌우
n = int(input())
A = list(input())
x = 1
y = 1
for i in A:  
  if i == 'R':
    y += 1
    if y > n:
      y -= 1
  elif i == 'L':
    y -= 1
    if y < 1:
      y += 1
  elif i == 'U':
    x -= 1
    if x < 1:
      x += 1
  elif i == 'D':
    x += 1
    if x > n:
      x -= 1
  else:
    continue
  
print(x, y)