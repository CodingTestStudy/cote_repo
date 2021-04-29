def solution(array, commands):
    answer = []
    for value in commands:
        temp = []
        for i in range(value[0] - 1, value[1]):
            temp.append(array[i])
        temp.sort()
        answer.append(temp[value[2] - 1])

    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])