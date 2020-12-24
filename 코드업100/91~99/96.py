# 96
n = int(input())
board = [[0] * 19 for _ in range(19)]
m_list = []
for i in range(n):
  x = list(map(int, input().split()))
  board[x[0] - 1][x[1] - 1] = 1

print(board)

