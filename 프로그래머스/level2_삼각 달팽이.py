# 못 푼 문제

def location(x, y, i):
    if i % 3 == 0:
        x += 1
    elif i % 3 == 1:
        y += 1
    else:
        x -= 1
        y -= 1
    return x, y

def solution(n):
    snail = [[0 for _ in range(1, i + 1)] for i in range(1, n + 1)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            x, y = location(x, y, i)
            snail[x][y] = num
            num += 1

    answer = []
    for i in range(n):
        for j in range(i + 1):
            answer.append(snail[i][j])
    return answer


print(solution(4))
print(solution(5))
print(solution(6))