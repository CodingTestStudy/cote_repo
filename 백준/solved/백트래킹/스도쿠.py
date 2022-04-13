import sys

input = sys.stdin.readline
sudoku = []

for _ in range(9):
    sudoku.append(list(map(int, input().split())))

blank_list = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank_list.append((i, j))


def check_row(r, target):
    for i in range(9):
        if sudoku[r][i] == target:
            return False
    return True


def check_col(c, target):
    for i in range(9):
        if sudoku[i][c] == target:
            return False
    return True


def check_box(r, c, target):
    r = r // 3 * 3
    c = c // 3 * 3
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if sudoku[i][j] == target:
                return False
    return True


def dfs(idx):
    if idx == len(blank_list):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end=' ')
            print()
        return

    for i in range(1, 10):
        r = blank_list[idx][0]
        c = blank_list[idx][1]
        if check_row(r, i) and check_col(c, i) and check_box(r, c, i):
            sudoku[r][c] = i
            dfs(idx + 1)
            sudoku[r][c] = 0


dfs(0)
