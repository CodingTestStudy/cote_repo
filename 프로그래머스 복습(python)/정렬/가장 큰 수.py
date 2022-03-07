## 시간초과 ##
from itertools import permutations
def solution(numbers):
    answer = []
    numbers = [str(numbers[i]) for i in range(len(numbers))]
    iterator = permutations(numbers, len(numbers))
    for it in iterator:
        num = ''
        for i in range(len(it)):
            num += it[i]
        answer.append(int(num))
    answer.sort()
    return str(answer[-1])

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))