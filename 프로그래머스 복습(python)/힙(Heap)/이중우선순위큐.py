# -*- coding:utf-8 -*-
import heapq


def solution(operations):
    max_q = []
    min_q = []
    for i in range(len(operations)):
        order, num = operations[i].split(" ")
        if order == "I":
            heapq.heappush(max_q, -int(num))
            heapq.heappush(min_q, int(num))
        else:
            if not max_q:
                pass
            elif int(num) == 1:
                value = -(heapq.heappop(max_q))
                min_q.remove(value)
            else:
                value = heapq.heappop(min_q)
                max_q.remove(-value)
    if not min_q:
        return [0, 0]
    else:
        return [-heapq.heappop(max_q), heapq.heappop(min_q)]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))