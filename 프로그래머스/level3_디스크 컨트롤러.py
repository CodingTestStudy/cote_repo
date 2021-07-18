# 힙 사용 방법
import heapq

def solution(jobs):
    count, answer, last = 0, 0, -1
    q = []
    jobs.sort()

    # 시작 시간 초기화
    time = jobs[0][0]
    while count != len(jobs):
        for s, t in jobs:
            # 작업 가능한 시간이라면
            # last가 있는 이유: 작업이 겹치지 않기 위해
            if last < s <= time:
                heapq.heappush(q, (t, s))
        if q:
            count += 1
            last = time
            term, start = heapq.heappop(q)
            time += term
            answer += (time - start)
        # 바로 수행할 작업이 없다면
        else:
            time += 1

    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))

# 단순 리스트로 해결한 방법
# def solution(jobs):
#     answer = 0
#     start = 0  # 현재까지 진행된 작업 시간
#     length = len(jobs)
#     jobs = sorted(jobs, key=lambda x: x[1])
#
#     while jobs:
#         for i in range(len(jobs)):
#             # 다음 작업이 가능한 작업이라면(기다리고 있는 작업)
#             if jobs[i][0] <= start:
#                 start += jobs[i][1]
#                 answer += start - jobs[i][0]
#                 jobs.pop(i)
#                 break
#             # 해당 시점에 아직 작업이 들어오지 않은 경우
#             # 대기 상태
#             if i == len(jobs) - 1:
#                 start += 1
#     return answer // length
#
#
# print(solution([[0, 3], [1, 9], [2, 6]]))

# 오답 코드
# import heapq
#
# def solution(jobs):
#     length = len(jobs)
#     q = []
#     while jobs:
#         start, time = jobs.pop()
#         heapq.heappush(q, (start, time))
#
#     start, time = heapq.heappop(q)
#     now = time
#     end = time
#     repeat = length
#
#     while repeat - 1 != 0:
#         wait_list = []
#         while q:
#             s, t = heapq.heappop(q)
#             if now <= s:
#                 heapq.heappush(q, (s, t))
#                 break
#             else:
#                 wait_list.append((t, s))
#         wait_list.sort(reverse=True)
#         # 직전의 작업이 끝나고, 다음 작업 수행 시작이 가능한 작업들 중
#         # 소요 시간이 가장 짧은 작업을 선택
#         t, s = wait_list.pop()
#         while wait_list:
#             ti, st = wait_list.pop()
#             heapq.heappush(q, (st, ti))
#
#         if now < s:
#             heapq.heappush(q, (s, t))
#             now += 1
#             repeat += 1
#             continue
#
#         else:
#             # 이전 작업이 수행되는 동안 기다린 시간
#             wait_time = end - s
#
#             # 총 작업 시간에 해당 작업의 수행시간과 기다린 시간을 더함
#             now += t + wait_time
#
#             # 기다린 시간 축적됨
#             end += t
#             repeat -= 1
#
#     return now // length
#
# print(solution([[0, 3], [1, 9], [2, 6]]))
