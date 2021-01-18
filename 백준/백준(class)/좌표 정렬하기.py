import heapq
n = int(input())
q = []
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(q, (x, y))

while q:
    x, y = heapq.heappop(q)
    print(x, y)