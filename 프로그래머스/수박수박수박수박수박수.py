def solution(n):
    answer = ''
    odd = "수"
    even = "수박"
    for _ in range(n // 2):
        answer += even
    if n % 2 == 1:
        answer += odd

    return answer

print(solution(4))

# return "수박"*(n//2) + "수"*(n%2)