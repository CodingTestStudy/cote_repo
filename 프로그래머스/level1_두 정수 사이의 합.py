def solution(a, b):
    if a == b:
        return a

    return int((a + b) * ((abs(a - b) + 1) / 2))
print(solution(1, 10))