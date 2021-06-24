def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)

    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))

# 시간초과 (test case 10)
# def solution(number, k):
#     answer = ""
#     idx = 0
#     while k != len(number):
#         max_value = '0'
#         for i in range(idx, k + 1):
#             if number[i] == 9:
#                 max_value = 9
#                 idx = i + 1
#                 break
#
#             if number[i] > max_value:
#                 max_value = number[i]
#                 idx = i + 1
#         k += 1
#         answer += max_value
#     return answer

# 시간초과
# from itertools import combinations
#
# def solution(number, k):
#     order = list(combinations([i for i in range(len(number))], len(number) - k))
#     num_list = list(number)
#     max_value = 0
#     while order:
#         n_order = order.pop()
#         num_str = ""
#         for i in range(len(n_order)):
#             num_str += number[n_order[i]]
#         max_value = max(max_value, int(num_str))
#     return str(max_value)


