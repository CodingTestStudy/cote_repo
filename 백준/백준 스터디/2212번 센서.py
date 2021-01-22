import heapq
N = int(input())    # 센서 개수
K = int(input())    # 집중국 개수
location = sorted(list(map(int, input().split())))  # 센서 좌표
print(location)

gap = []
for i in range(len(location) - 1):
    heapq.heappush(gap, -(location[i + 1] - location[i]))
print(gap)
result = 0
for i in range(K - 1):
    x = -heapq.heappop(gap)
    print(x)
    result += x

if N <= K:
    print(0)
else: print(result)