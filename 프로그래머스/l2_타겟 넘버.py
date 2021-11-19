from collections import deque, Counter


def solution(numbers, target):
    numbers = deque(numbers)
    first = numbers.popleft()
    answer = deque([first, -first])

    while numbers:
        x = numbers.popleft()
        for i in range(len(answer)):
            y = answer.popleft()
            answer.append(y + x)
            answer.append(y - x)

    return Counter(answer)[target]

print(solution([1, 1, 1, 1, 1], 3))