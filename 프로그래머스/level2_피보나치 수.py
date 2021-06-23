def solution(n):
    if n == 0: return 0
    if n == 1: return 1
    fibonacci = [0, 1]
    for i in range(2, n + 1):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[n] % 1234567

# import sys
# sys.setrecursionlimit(100001)
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# def solution(n):
#     return fibonacci(n)

print(solution(3))
print(solution(5))