def solution(progresses, speeds):
    answer = []
    q = []

    for _ in range(len(progresses)):
        q.append(False)
    k = 0

    while sum(progresses) != 0:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                progresses[i] = 0
                speeds[i] = 0
                q[i] = True

        print(progresses)
        while k < len(q) and q[k]:
            k += 1
            cnt += 1

        if cnt != 0:
            answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# answer
# from collections import deque
# def solution(progresses, speeds):
#     answer = []
#     q = deque()
#     for _ in range(len(progresses)):
#         q.append(False)
#     k = 0
#
#     while sum(progresses) != 0:
#         count = 0
#         for i in range(len(progresses)):
#             progresses[i] += speeds[i]
#             if progresses[i] >= 100:
#                 progresses[i] = 0
#                 speeds[i] = 0
#                 q[i] = True
#
#         while k < len(q) and q[k]:
#             k += 1
#             count += 1
#
#         if count != 0:
#             answer.append(count)
#
#     return answer
