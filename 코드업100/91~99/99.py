# 99
# 개미집 초기화
home = [[0] * 10 for _ in range(10)]

# 입력값 삽입
for i in range(10):
  num = list(map(int, input().split()))
  for j in range(10):
    home[i][j] = num[j]


home[1][1] = 9
x = 1
y = 1
while x < 9:      
  if home[x][y+1] == 0:    
    home[x][y+1] = 9    
    y += 1        
    continue
  elif home[x][y+1] == 1:    
    if(home[x+1][y] == 2): 
      home[x+1][y] = 9
      break
    else:
      home[x+1][y] = 9    
      x += 1      
      continue
    
print(home)