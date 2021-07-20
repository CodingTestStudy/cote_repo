def change(s):
    p = list('110')
    length = len(s)

    # 110 제거
    count = 0
    stack = []
    for i in range(length):
        stack.append(s[i])
        if stack[-3:] == p:
            stack.pop()
            stack.pop()
            stack.pop()

    stack_length = len(stack)
    count = int((length - stack_length)/3)

    # 110 붙이기
    for i in range(stack_length + 1):
        temp = (stack[i:i+3]*3)[:3]
        if temp > p:
            break
    result = stack[:i] + p*count + stack[i:]
    return ''.join(result)

def solution(s):
    answer = [change(s_) for s_ in s]
    return answer

print(solution(["1110", "100111100", "0111111010"]))
