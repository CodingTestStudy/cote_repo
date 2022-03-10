from collections import deque, Counter


def solution(numbers, target):
    numbers = deque(numbers)
    q = deque()
    q.append(0)
    while numbers:
        num = numbers.popleft()
        for _ in range(len(q)):
            x = q.popleft()
            q.append(x + num)
            q.append(x - num)
    return Counter(q)[target]


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))