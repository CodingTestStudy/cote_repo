def solution(triangle):
    answer = 0
    for i in range(len(triangle) - 1):
        triangle[i + 1][0] += triangle[i][0]
        for j in range(1, i + 1):
            triangle[i + 1][j] += max(triangle[i][j - 1], triangle[i][j])
        triangle[i + 1][i + 1] += triangle[i][i]
        print(triangle)
    for value in triangle[len(triangle) - 1]:
        answer = max(answer, value)
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
