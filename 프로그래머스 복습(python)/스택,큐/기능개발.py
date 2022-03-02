import math


def solution(progresses, speeds):
    answer = []
    end_time_list = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    now = 0
    for i in range(len(end_time_list)):
        if end_time_list[i] > end_time_list[now]:
            answer.append(i - now)
            now = i
    answer.append(len(end_time_list) - now)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# def solution(progresses, speeds):
#     answer = []
#     q = []
#     for _ in range(len(progresses)):
#         q.append(False)
#     idx = 0
#
#     while sum(progresses) != 0:
#         cnt = 0
#         for i in range(len(progresses)):
#             progresses[i] += speeds[i]
#             if progresses[i] >= 100:
#                 progresses[i] = 0
#                 speeds[i] = 0
#                 q[i] = True
#
#         print(progresses)
#         while idx < len(q) and q[idx]:
#             idx += 1
#             cnt += 1
#
#         if cnt != 0:
#             answer.append(cnt)
#
#     return answer
