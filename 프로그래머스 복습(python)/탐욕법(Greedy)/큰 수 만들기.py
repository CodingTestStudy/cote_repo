# -*- coding:utf-8 -*-

# 못 푼 문제
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
        print(f"number -> {number}, {stack}")

    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
