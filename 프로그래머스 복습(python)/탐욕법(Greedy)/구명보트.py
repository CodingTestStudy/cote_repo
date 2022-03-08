from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        max_weight = people.pop()
        if people and people[0] + max_weight <= limit:
            people.popleft()
        answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))