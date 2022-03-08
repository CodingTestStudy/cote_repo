# -*- coding:utf-8 -*-
def solution(n, lost, reserve):
    temp_lost = dict() # 여벌옷 받았는지 여부
    temp_reserve = dict() # 여벌옷 빌려줬는지 여부

    for value in lost:
        temp_lost[value] = False
    for value in reserve:
        temp_reserve[value] = False
        # 여벌이 있는 학생중에서 옷을 잃어버린 경우
        if value in lost:
            temp_reserve[value] = True
            temp_lost[value] = True

    # 앞, 뒤에만 여벌 체육복 있는 경우 먼저 처리
    for target in lost:
        if (target - 1) in reserve and (target + 1) in reserve:
            pass
        elif (target - 1) in reserve and not temp_reserve[target - 1]:
            temp_lost[target] = True
            temp_reserve[target - 1] = True
        elif (target + 1) in reserve and not temp_reserve[target + 1]:
            temp_lost[target] = True
            temp_reserve[target + 1] = True

    # 나머지 경우 처리
    for target in lost:
        if not temp_lost[target]:
            if (target - 1) in reserve and not temp_reserve[target - 1]:
                temp_lost[target] = True
                temp_reserve[target - 1] = True
            elif (target + 1) in reserve and not temp_reserve[target + 1]:
                temp_lost[target] = True
                temp_reserve[target + 1] = True

    for target in lost:
        if not temp_lost[target]:
            n -= 1
    return n


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(7, [2, 3, 4], [1, 2, 3, 6]))