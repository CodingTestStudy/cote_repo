import heapq
import sys

N = int(input())
data = []
for _ in range(N):
    data.append((list(map(int, sys.stdin.readline().rstrip().split()))))

data.sort()
q = []

for s, t in data:
    heapq.heappush(q, t)
    if q[0] <= s:
        heapq.heappop(q)

result = len(q)
print(result)