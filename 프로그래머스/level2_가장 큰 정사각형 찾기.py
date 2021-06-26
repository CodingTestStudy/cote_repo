# 못푼 문제(dp 활용해야 함)

def solution(board):
    # 1X1 인 경우
    if len(board) == 1 and len(board[0]) == 1:
        if board[0][0] == 1:
            return 1
        else:
            return 0

    max_length = 0
    for r in range(len(board) - 1):
        for c in range(len(board[0]) - 1):
            if board[r + 1][c + 1] != 0:
                board[r + 1][c + 1] = min(board[r][c], board[r + 1][c], board[r][c + 1]) + 1
                max_length = max(max_length, board[r + 1][c + 1])
    return max_length * max_length

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[1, 0], [0, 0]]))