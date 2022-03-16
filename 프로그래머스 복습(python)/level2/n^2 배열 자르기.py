def solution(n, left, right):
    answer = []

    # test 12,13 int로 감싸야 통과됨
    r1, c1 = int(left) // n, int(left) % n
    r2, c2 = int(right) // n, int(right) % n
    for i in range(r1 + 1, r2 + 2):
        for j in range(i):
            answer.append(i)
        for j in range(i + 1, n + 1):
            answer.append(j)
    return answer[c1:(r2 - r1) * n + c2 + 1]


print(solution(3, 2, 5))
print(solution(4, 7, 14))

# # more simple code
# def solution(n, left, right):
#     answer = []
#     for i in range(left,right+1):
#         answer.append(max(i//n,i%n)+1)
#     return answer


# # 시간초과
# def solution(n, left, right):
#     temp = [[1] * (n + 1) for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             temp[j][i] = i
#             temp[i][j] = i
#     answer = []
#     for i in range(1, n + 1):
#         answer.extend(temp[i][1:])
#     return answer[left:right + 1]
