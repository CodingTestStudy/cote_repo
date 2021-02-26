import sys
N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
result = []

# case1 막대기(가로, 세로)
def case1():
    max_value = -1e9
    for i in range(N):
        for j in range(M):
            sum_value1 = 0
            sum_value2 = 0
            for k in range(4):
                # 범위를 벗어나는 경우 pass
                # 각각 가로 막대기, 세로 막대기인 경우의 합들을 구한 후
                try: sum_value1 += board[i][j + k]
                except: pass
                try: sum_value2 += board[i + k][j]
                except: pass
            # 최댓값을 선정하여, result 리스트에 삽입
            sum_value = max(sum_value1, sum_value2)
            max_value = max(max_value, sum_value)
    result.append(max_value)


# case2 그 외의 도형
# 2x3, 3x2의 도형을 임의로 만든 후
# 해당 범위에서 필요없는 부분을 빼가면서, 모든 도형의 합을 temp 리스트에 삽입
# temp 리스트 중 최대값을 result 리스트에 삽입
def case2():
    temp = []
    # 모든 범위에 대해서
    for i in range(N):
        for j in range(M):
            sum_value = 0

            # 2x3 도형
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
                # 대각선 모양
                temp.append(sum_value - board[i][j] - board[i + 1][j + 2])
                temp.append(sum_value - board[i][j + 2] - board[i + 1][j])
            except:
                pass

            sum_value = 0
            # 3x2 도형
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
                # 대각선 모양
                temp.append(sum_value - board[i][j] - board[i + 2][j + 1])
                temp.append(sum_value - board[i][j + 1] - board[i + 2][j])
            except:
                pass

    result.append(max(temp))

case1()
case2()
print(max(result))