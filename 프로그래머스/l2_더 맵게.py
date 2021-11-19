import heapq


def solution(scoville, K):
    time = 0
    heapq.heapify(scoville)
    first = heapq.heappop(scoville)

    while scoville and first < K:
        second = heapq.heappop(scoville)
        new_data = first + second * 2
        time += 1
        heapq.heappush(scoville, new_data)
        first = heapq.heappop(scoville)

    if first < K:
        return -1
    return time

print(solution([1, 2, 3, 9, 10, 12], 7))