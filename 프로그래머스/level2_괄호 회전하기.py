def solution(s):
    answer = 0
    for i in range(len(s)):
        flag = True
        temp = s[i:] + s[:i]
        stack = []
        for j in range(len(temp)):
            if temp[j] in {'[', '(', '{'}:
                stack.append(temp[j])
            else:
                # 처음부터 잘못된 괄호 문자열인 경우
                if len(stack) == 0:
                    flag = False
                    break
                # 그 외의 적절한 괄호 문자열을 만났을 경우, 같이 지워진다.
                elif temp[j] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                elif temp[j] == ')':
                    if stack[-1] == '(':
                        stack.pop()
                elif temp[j] == '}':
                    if stack[-1] == '{':
                        stack.pop()
        if flag and len(stack) == 0:
            answer += 1
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
