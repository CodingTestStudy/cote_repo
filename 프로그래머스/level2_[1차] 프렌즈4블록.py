def check_around(block, i, j, text):
    if block[i - 1][j] == text and block[i - 1][j + 1] == text and i - 1 >= 0:
        return True
    return False

def solution(m, n, board):
    answer = 0
    delete_list = []
    block = [[] for _ in range(m)]
    flag = True
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            block[i].append(board[i][j])

    while flag:
        flag = False
        for i in range(m - 1, -1, -1):
            for j in range(n - 1):
                if block[i][j] == block[i][j + 1] and block[i][j] != "X":
                    # 4개가 동일한 경우
                    if check_around(block, i, j, block[i][j]):
                        flag = True
                        delete_list.append((i, j))
                        delete_list.append((i - 1, j))
                        delete_list.append((i, j + 1))
                        delete_list.append((i - 1, j + 1))

        while delete_list:
            x, y = delete_list.pop()
            block[x][y] = " "

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                count = 0
                if block[i][j] == " ":
                    for k in range(i, -1, -1):
                        if block[k][j] == " ":
                            count += 1
                            answer += 1
                        else:
                            break

                    for k in range(i, -1, -1):
                        nxt = k - count
                        if nxt < 0:
                            block[k][j] = "X"
                        else:
                            block[k][j] = block[nxt][j]
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(2, 4, ["baab", "baab"]))
print(solution(6, 6, ["IIIIOO", "IIIOOO", "IIIOOI", "IOOIII", "OOOIII", "OOIIII"]))