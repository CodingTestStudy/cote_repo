def solution(n,a,b):
    count = 1
    if a > b:
        a, b = b, a
    while b - a != 1 or (b + a) % 4 != 3:
        count += 1
        a = sum(divmod(a, 2))
        b = sum(divmod(b, 2))

    return count

print(solution(8, 1, 2))
print(solution(8, 2, 3))
print(solution(8, 4, 7))


# def solution(n,a,b):
#     answer = 0
#     while a != b:
#         answer += 1
#         a, b = (a+1)//2, (b+1)//2
#
#     return answer