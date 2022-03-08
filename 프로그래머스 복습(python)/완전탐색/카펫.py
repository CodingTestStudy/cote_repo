def solution(brown, yellow):
    xy = brown + yellow
    y = 2
    while True:
        if xy % y == 0 and y == (brown + 4) / 2 - xy / y:
            return [xy / y, y]
        y += 1


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

# 이전 코드
def solution(brown, yellow):
    for r in range(brown, 0, -1):
        for c in range(r, 0, -1):
            if (r-2) * (c-2) == yellow and brown + yellow == r * c:
                return [r, c]