def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start, end, k = commands[i]
        temp = [array[j] for j in range(start - 1, end)]
        temp.sort()
        answer.append(temp[k - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


def solution(array, commands):
    answer = []
    for value in commands:
        temp = []
        for i in range(value[0] - 1, value[1]):
            temp.append(array[i])
        temp.sort()
        answer.append(temp[value[2] - 1])

    return answer