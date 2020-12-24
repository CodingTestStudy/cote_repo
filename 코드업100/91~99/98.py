# 98
# 격자판 가로, 세로
w, h = map(int, input().split())
board = [[0] * w for _ in range(h)]
# 막대의 개수
n = int(input())
# 막대의 길이(l), 방향(d), 좌표(x, y)
# d = 0, 1 -> 가로, 세로
for i in range(n):
  l, d, x, y = map(int, input().split())
  for j in range(l):
   if d == 0: board[x-1][y-1+j] = 1      
   else: board[x-1+j][y-1] = 1 
 
print(board)