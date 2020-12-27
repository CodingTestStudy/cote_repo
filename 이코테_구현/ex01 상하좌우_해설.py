# 상하좌우
n = int(input())
plans = list(input())

# L, R, U, D
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x = 1
y = 1
nx = 0
ny = 0

# 이동계획 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range (len(move_types)):
    if move_types[i] == plan:      
      nx = x + dx[i]
      ny = y + dy[i]   
    # 공간 벗어나는 경우, 좌표 갱신하지 않고 무시      
    if not (1 <= nx <= n and 1 <= ny <= n):     
      continue    
    # 좌표 갱신        
    x, y = nx, ny      

print(x, y)    
  