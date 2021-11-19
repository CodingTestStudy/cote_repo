from collections import deque


def solution(rows, columns, queries):
    square = [[] for _ in range(rows + 1)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            square[i].append(num)
            num += 1

    min_list = []
    queries = deque(queries)
    while queries:
        x1, y1, x2, y2 = queries.popleft()
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        temp1 = square[x1][y2]
        for j in range(y2, y1, -1):
            square[x1][j] = square[x1][j - 1]

        temp2 = square[x2][y2]
        for j in range(x2, x1 + 1, -1):
            square[j][y2] = square[j - 1][y2]
        square[x1 + 1][y2] = temp1

        temp3 = square[x2][y1]
        for j in range(y1, y2 - 1):
            square[x2][j] = square[x2][j + 1]
        square[x2][y2 - 1] = temp2

        for j in range(x1, x2 - 1):
            square[j][y1] = square[j + 1][y1]
        square[x2 - 1][y1] = temp3

        min_value = 10001
        for j in range(y1, y2 + 1):
            min_value = min(min_value, square[x1][j])
            min_value = min(min_value, square[x2][j])
        for j in range(x1, x2 + 1):
            min_value = min(min_value, square[j][y1])
            min_value = min(min_value, square[j][y2])
        min_list.append(min_value)
    return min_list


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))
