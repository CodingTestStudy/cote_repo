import heapq
N = int(input())
K = int(input())
location = sorted(list(map(int, input().split())))

if N <= K: print(0)
else:
    gap = []
    for i in range(len(location) - 1):
        heapq.heappush(gap, -(location[i + 1] - location[i]))   
    result = 0
    for i in range(K - 1):       
        heapq.heappop(gap)
    print(-sum(gap))
