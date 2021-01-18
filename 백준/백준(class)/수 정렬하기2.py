import heapq, sys
input = sys.stdin.readline
n = int(input())
q = []
result = []
for _ in range(n):
    heapq.heappush(q, int(input()))

while q:
   print(heapq.heappop(q))