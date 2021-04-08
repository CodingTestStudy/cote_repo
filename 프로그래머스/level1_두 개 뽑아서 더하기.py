def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            x = numbers[i] + numbers[j]
            if x not in answer:
                answer.append(x)

    answer.sort()
    return answer