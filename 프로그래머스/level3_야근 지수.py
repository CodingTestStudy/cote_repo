import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0

    answer = 0
    q = []
    while works:
        heapq.heappush(q, -works.pop())
    for i in range(n):
        x = -heapq.heappop(q)
        heapq.heappush(q, -(x - 1))

    while q:
        answer += q.pop() ** 2
    return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
# 효울성 시간 초과
# def solution(n, works):
#     answer = 0
#     for i in range(n):
#         works.sort()
#         works[-1] -= 1
#         if sum(works) == 0:
#             return 0
#     for value in works:
#         answer += value ** 2
#
#     return answer