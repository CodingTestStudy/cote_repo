def solution(s):
    temp = []
    for i in s:
        if not temp:
            temp.append(i)
        elif temp[-1] == i:
            temp.pop()
        else:
            temp.append(i)
        print(temp)

    if not temp:
        return 1
    else:
        return 0

print(solution("baabaa"))