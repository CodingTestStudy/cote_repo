import heapq


def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        first_value = heapq.heappop(scoville)
        if first_value >= k:
            return answer
        if scoville:
            second_value = heapq.heappop(scoville)
            new_value = first_value + (second_value * 2)
            heapq.heappush(scoville, new_value)
            answer += 1

    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))

import heapq
def solution(scoville, K):
    time = 0
    heapq.heapify(scoville)

    first = heapq.heappop(scoville)

    while scoville and first < K:
        second = heapq.heappop(scoville)
        new_food = first + second * 2
        heapq.heappush(scoville, new_food)
        first = heapq.heappop(scoville)
        time += 1

    if first < K:
        return -1
    return time