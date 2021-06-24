def solution(s):
    check = 0
    for i in range(len(s)):
        if s[i] == '(':
            check += 1
        else:
            check -= 1

        # ')'가 더 많이 나온 경우
        if check < 0:
            return False

    # 위 반복문에서 ')'의 개수가 더 많은 경우가 있는지 확인했기 때문에
    # '('가 더 많은 경우
    if check != 0:
        return False

    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))