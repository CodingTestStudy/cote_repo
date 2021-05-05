def solution(progresses, speeds):
    answer = []
    q = []
    for _ in range(len(progresses)):
        q.append(False)
    k = 0

    while sum(progresses) != 0:
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                progresses[i] = 0
                speeds[i] = 0
                q[i] = True

        while k < len(q) and q[k]:
            k += 1
            count += 1

        if count != 0:
            answer.append(count)

    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))

# from collections import deque
# def solution(progresses, speeds):
#     progresses = deque(progresses)
#     speeds = deque(speeds)
#     answer = []
#     time = 0
#     count = 0
#     while progresses:
#         if (progresses[0] + time*speeds[0]) >= 100:
#             progresses.popleft()
#             speeds.popleft()
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer
