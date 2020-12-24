# 97
# 바둑판 생성
board = [[0] * 19 for _ in range(19)]

# 입력값 바둑판에 넣기
for i in range(19):
  num = list(map(int, input().split()))
  for j in range(19):
    board[i][j] = num[j]


n = int(input())

for i in range(n):
  x = list(map(int, input().split()))
  for j in range(19):
    if board[x[0] - 1][j] == 1: board[x[0] - 1][j] = 0
    else: board[x[0] - 1][j] = 1

    if board[j][x[1] - 1] == 1: board[j][x[1] - 1] = 0
    else: board[j][x[1] - 1] = 1

print(board)