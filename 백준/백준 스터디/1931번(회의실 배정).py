import sys
import heapq

input = sys.stdin.readline
n = int(input())
x = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(x, (a, b))

x.sort()
max_count = 0
while x:
    first_value, last_value = heapq.heappop(x)
    count = 1
    last = last_value
    j = 1
    while True:
        if j < len(x):
            if x[j][0] >= last:
                last = x[j][1]
                j += 1
                count += 1
            else:
                j += 1
        else:
            max_count = max(max_count, count)
            break

print(max_count)