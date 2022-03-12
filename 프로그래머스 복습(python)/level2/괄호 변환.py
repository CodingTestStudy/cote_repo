def divide(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i + 1], p[i + 1:]


def check(u):
    stack = []
    for value in u:
        if value == '(':
            stack.append(value)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    if not p:
        return ""
    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for value in u[1:len(u) - 1]:
            if value == '(':
                answer += ')'
            else:
                answer += '('
        return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
