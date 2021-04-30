def solution(n):
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i != n // i:
                answer += i + n // i
            else:
                answer += i
    return answer

print(solution(5))

# return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])