def solution(brown, yellow):
    for r in range(brown, 0, -1):
        for c in range(r, 0, -1):
            if (r-2) * (c-2) == yellow and brown + yellow == r * c:
                return [r, c]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
