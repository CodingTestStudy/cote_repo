def solution(rows, columns, queries):
    answer = [[] * (columns + 1) for _ in range(rows)]
    min_list = []

    # 행렬 생성
    for i in range(rows):
        for j in range(1, columns + 1):
            answer[i].append(i * columns + j)

    # 주어진 queries 다루는 반복문
    for i in range(len(queries)):
        x1 = queries[i][0] - 1
        y1 = queries[i][1] - 1
        x2 = queries[i][2] - 1
        y2 = queries[i][3] - 1

        # 왼 -> 오
        temp1 = answer[x1][y2]
        for j in range(y2, y1, -1):
            answer[x1][j] = answer[x1][j - 1]

        # 위 -> 아래
        temp2 = answer[x2][y2]
        for j in range(x2, x1 + 1, -1):
            answer[j][y2] = answer[j - 1][y2]
        answer[x1 + 1][y2] = temp1

        # 오 -> 왼
        temp3 = answer[x2][y1]
        for j in range(y1, y2 - 1):
            answer[x2][j] = answer[x2][j + 1]
        answer[x2][y2 - 1] = temp2

        # 아래 -> 위
        for j in range(x1, x2 - 1):
            answer[j][y1] = answer[j + 1][y1]
        answer[x2 - 1][y1] = temp3


        # 최소값 찾기
        min_value = 10001
        for i in range(y1, y2 + 1):
            min_value = min(answer[x1][i], min_value)
            min_value = min(answer[x2][i], min_value)
        for i in range(x1, x2 + 1):
            min_value = min(answer[i][y1], min_value)
            min_value = min(answer[i][y2], min_value)
        min_list.append(min_value)

    return min_list


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1,1, 100, 97]]))
