from collections import deque


def solution(priorities, location):
    prio_list = deque()
    answer = {}
    sort = 0
    for index in range(len(priorities)):
        prio_list.append([priorities[index], index])

    while prio_list:
        target, index = prio_list.popleft()
        flag = False
        for t, v in prio_list:
            if t > target:
                prio_list.append([target, index])
                flag = True
                break
        if not flag:
            answer[index] = sort
            sort += 1
    return answer[location] + 1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))