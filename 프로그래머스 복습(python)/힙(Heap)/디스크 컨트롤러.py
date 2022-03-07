# -*- coding:utf-8 -*-
import heapq


def solution(jobs):
    answer = 0
    time = 0
    count = 0
    condition = [False] * len(jobs)
    q = []
    while count != len(jobs):
        for i in range(len(jobs)):
            s, t = jobs[i][0], jobs[i][1]
            if not condition[i] and s <= time:
                heapq.heappush(q, [t, s])
                condition[i] = True
        if q:
            count += 1
            t, s = heapq.heappop(q)
            time += t
            answer += (time - s)
        else:
            time += 1

    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))