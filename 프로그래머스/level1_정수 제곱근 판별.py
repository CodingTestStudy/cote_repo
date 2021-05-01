def solution(n):
    if n ** 0.5 - int(n ** 0.5) == 0:
        return (int(n ** 0.5) + 1) ** 2
    return -1

print(solution(3))

# 연산 결과와 1로 나눈 나머지의 값이 0이면, 정수
# 굳이 한번 더 연산해서 뺄셈할 필요 X
# def nextSqure(n):
#     sqrt = n ** (1/2)
#
#     if sqrt % 1 == 0:
#         return (sqrt + 1) ** 2
#     return 'no'