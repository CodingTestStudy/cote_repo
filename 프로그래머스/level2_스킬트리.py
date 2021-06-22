def solution(skill, skill_trees):
    answer = len(skill_trees)
    temp = []
    for i in range(len(skill)):
        temp.append(i)
    skill_dict = dict(zip(skill, temp))
    for value in skill_trees:
        check_list = [False] * len(skill)
        flag = True
        for i in range(len(value)):
            if value[i] in skill:
                check_list[skill_dict[value[i]]] = True
                for j in range(skill_dict[value[i]]):
                    if not check_list[j]:
                        answer -= 1
                        flag = False
                        break
                if not flag:
                    break

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))

#another solution
from collections import deque
def another_solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = deque(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.popleft():
                    break
        else:
            answer += 1

    return answer
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(another_solution(skill, skill_trees))