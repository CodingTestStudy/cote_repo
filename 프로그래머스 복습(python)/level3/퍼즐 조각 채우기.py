import copy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def rotated(board):
    length = len(board)
    result = []
    for b in board:
        result.append([b[1], length - 1 - b[0]])
    return sorted(move_to_standard(result, length))


def dfs(table, r, c, temp, a, b):
    if r < 0 or r >= n or c < 0 or c >= n:
        return False
    if table[r][c] == a:
        temp.append([r, c])
        table[r][c] = b
        for i in range(4):
            dfs(table, r + dr[i], c + dc[i], temp, a, b)
        return True
    return False


# [0. 0] 기준으로 도형, 빈 공간 옮기기
def move_to_standard(board, length):
    change_list = []
    min_r = length
    min_c = length
    for r, c in board:
        min_r = min(min_r, r)
        min_c = min(min_c, c)
    for r, c, in board:
        change_list.append([r - min_r, c - min_c])
    return sorted(change_list)


def solution(game_board, table):
    global n
    n = len(table)
    answer = 0

    # game_board 내의 빈 공간 리스트
    game_list = []
    for r in range(n):
        for c in range(n):
            if table[r][c] == 0:
                g = []
                dfs(game_board, r, c, g, 0, 1)
                if g:
                    game_list.append(g)

    # [0, 0] 으로 위치 이동
    changed_game_list = []
    for emp in game_list:
        changed_game_list.append(move_to_standard(emp, n))

    # table 내의 조각 리스트
    table_list = []
    for r in range(n):
        for c in range(n):
            if table[r][c] == 1:
                t = []
                dfs(table, r, c, t, 1, 0)
                if t:
                    table_list.append(t)

    changed_table_list = []
    for sh in table_list:
        changed_table_list.append(move_to_standard(sh, n))

    for game in changed_game_list:
        flag = False
        for table in changed_table_list:
            temp = copy.copy(table)
            for _ in range(4):
                temp = rotated(temp)
                if game == temp:
                    answer += len(game)
                    changed_table_list.remove(table)
                    flag = True
                    break
            if flag:
                break
    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))
