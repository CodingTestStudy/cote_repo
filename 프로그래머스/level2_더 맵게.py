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

scoville = [1, 2, 3]
K = 11
print(solution(scoville, K))