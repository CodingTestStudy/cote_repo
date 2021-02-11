import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
result = []

# case1 막대기
def case1():
    max_value = -1e9
    for i in range(N):
        for j in range(M):
            sum_value1 = 0
            sum_value2 = 0
            for k in range(4):
                try: sum_value1 += board[i][j + k]
                except: pass
                try: sum_value2 += board[i + k][j]
                except: pass
            sum_value = max(sum_value1, sum_value2)
            max_value = max(max_value, sum_value)
    result.append(max_value)


def case2():
    temp = []
    max_value = -1e9
    for i in range(N):
        for j in range(M):
            sum_value = 0
            for k in range(2):
                for l in range(3):
                    try: sum_value += board[i + k][j + l]
                    except:
                        sum_value = 0
                        pass
            try:
                # 네모
                temp.append(sum_value - board[i][j] - board[i + 1][j])
                temp.append(sum_value - board[i][j + 2] - board[i + 1][j + 2])
                # ㄴ, ㅗ
                temp.append(sum_value - board[i][j] - board[i][j + 1])
                temp.append(sum_value - board[i][j + 1] - board[i][j + 2])
                temp.append(sum_value - board[i + 1][j] - board[i + 1][j + 1])
                temp.append(sum_value - board[i + 1][j + 1] - board[i + 1][j + 2])
                temp.append(sum_value - board[i][j] - board[i][j + 2])
                temp.append(sum_value - board[i + 1][j] - board[i + 1][j + 2])
                # 대각선
                temp.append(sum_value - board[i][j] - board[i + 1][j + 2])
                temp.append(sum_value - board[i][j + 2] - board[i + 1][j])
            except:
                sum_value = 0
                pass
            sum_value = 0
            for k in range(3):
                for l in range(2):
                    try:
                        sum_value += board[i + k][j + l]
                    except:
                        sum_value = 0
                        pass
            try:
                # 네모
                temp.append(sum_value - board[i][j] - board[i][j + 1])
                temp.append(sum_value - board[i + 2][j] - board[i + 2][j + 1])
                # ㄴ, ㅗ
                temp.append(sum_value - board[i][j] - board[i + 1][j])
                temp.append(sum_value - board[i][j + 1] - board[i + 1][j + 1])
                temp.append(sum_value - board[i + 1][j] - board[i + 2][j])
                temp.append(sum_value - board[i + 1][j + 1] - board[i + 2][j + 1])
                temp.append(sum_value - board[i][j] - board[i + 2][j])
                temp.append(sum_value - board[i][j + 1] - board[i + 2][j + 1])
                # 대각선
                temp.append(sum_value - board[i][j] - board[i + 2][j + 1])
                temp.append(sum_value - board[i][j + 1] - board[i + 2][j])
            except:
                sum_value = 0
                pass

    result.append(max(temp))

case1()
case2()
print(max(result))