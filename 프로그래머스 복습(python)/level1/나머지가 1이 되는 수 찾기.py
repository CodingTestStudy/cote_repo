def solution(n):
    for i in range(1, n):
        if n % i == 1:
            return i


print(solution(10))
print(solution(12))
