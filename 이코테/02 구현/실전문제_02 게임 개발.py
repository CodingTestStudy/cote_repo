# 게임 개발
# d = 0(북), 1(동), 2(남), 3(서) -> d % 4
# d는 index로 활용할 예정

row, column = map(int, input().split()) 
x, y, d = map(int, input().split())
result = 1 # 현재 위치도 방문한 칸이다.
turn = 0
nx = 0
ny = 0
# 맵 초기화
# 0 : 육지, 1 : 바다, 2 : 지나간 곳
game_map = [[0] * column for _ in range(row)]

# 북, 동, 남, 서
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(row):
  row_data = list(map(int, input().split()))
  game_map[i] = row_data

while True:    
  # 이동할 좌표가 범위를 벗어났는지 확인
  if not(0 <= x + move[d][0] < column and 0 <= y + move[d][1] < row):
    print("범위 벗어남")
    break
  # 이동 위치가 육지이고, 이전에 가본 칸이 아니라면
  if game_map[x + move[d][0]][y + move[d][1]] == 0:    
    # 이동    
    nx += x + move[d][0]
    ny += y + move[d][1]
            
    game_map[x][y] = 2 # 방문했다는 의미      
    x = nx
    y = ny 
    nx = 0
    ny = 0               
    
    result += 1 # 방문 횟수 증가    
    # 회전 및 방향 설정
    d += 1
    d %= 4
    turn = 0 # 이전에 막혀서 회전했던 일이 있었으면, 초기화 해줘야 함
    
  # 이동 위치가 바다거나 왔던 곳이라면, 방향 이동
  else:
    # 네 방향 모두 바다거나 가본 칸이라면
    if turn == 4:
      # 뒤로 이동    
      turn = 0  
      nx += x + move[(d + 2) % 4][0]
      ny += y + move[(d + 2) % 4][1]
      # 범위 확인
      if nx < 0 or nx > column or ny < 0 or ny > row:
        break

      # 뒤로 이동했는데 바다라면 종료    
      if game_map[nx][ny] == 1:       
        break
      # 뒤가 바다가 아니라면, 뒤로 이동 후, 다시 turn        
      else:
        x = nx
        y = ny
        # 갈 곳이 없어 회전한 횟수 증가
        turn += 1
        continue
    # 단순히 회전      
    else:
      turn += 1
      d += 1
      d %= 4

print(result)


    

    