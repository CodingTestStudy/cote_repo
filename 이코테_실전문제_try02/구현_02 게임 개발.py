# 게임 개발
# 3 <= n, m <= 50
# 0, 1, 2, 3 -> 북, 동, 남, 서
# 0, 1, 2 : 육지, 바다, 가본 곳
n, m = map(int, input().split())
x, y, d = map(int, input().split())
count = 0
turn = 0
game_map = []
for _ in range(n):
  game_map.append(list(map(int, input().split())))

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 북, 동, 남, 서
game_map[y][x] = 2
count += 1
while 0 <= x < m and 0 <= y < n:    
  print(game_map)
  d = (d + 1) % 4
  nx = x + direction[d][0]
  ny = y + direction[d][1]
  if 0 <= nx < m and 0 <= ny < n:
    if game_map[ny][nx] < 1:
      x = nx
      y = ny
      game_map[y][x] = 2
      count += 1
      turn = 0    
    else:
      turn += 1
      if turn == 4:
        turn = 0
        nd = (d + 2) % 4
        nx = x + direction[nd][0]
        ny = y + direction[nd][1]
        if not(0 <= nx < m and 0 <= ny < n) or game_map[ny][nx] > 0:          
          break
        if game_map[ny][nx] == 0:
          game_map[ny][nx] = 2
          count += 1
        x = nx
        y = ny
        d = nd      
  else:
    turn += 1
    if turn == 4:
      print("out of range")
      break

print(count)


  