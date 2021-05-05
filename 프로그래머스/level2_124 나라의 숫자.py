def solution(n):
    if n <= 3:
        return '124'[n - 1]
    else:
        q, r = divmod(n - 1, 3)
        return solution(q) + '124'[r]

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))

# def change124(n):
#     num = ['1','2','4']
#     answer = ""
#     while n > 0:
#         n -= 1
#         answer = num[n % 3] + answer
#         n //= 3
#     return answer