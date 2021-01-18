n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

even_digit = 'W'
odd_digit = 'B'
min_error = n * m
for i in range(n - 8 + 1): # 10 - 8 = 2 (0~2) 3번
    for j in range(m - 8 + 1): # 13 - 8 = 5 (0~5) 6번
        error1 = 0
        error2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0 and board[a][b] == odd_digit:
                    error1 += 1
                elif (a + b) % 2 == 1 and board[a][b] == even_digit:
                    error1 += 1

                if (a + b) % 2 == 0 and board[a][b] == even_digit:
                    error2 += 1
                elif (a + b) % 2 == 1 and board[a][b] == odd_digit:
                    error2 += 1

        error = min(error1, error2)
        min_error = min(error, min_error)


print(min_error)