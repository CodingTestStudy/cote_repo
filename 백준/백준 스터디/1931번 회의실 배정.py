import sys
import heapq
input = sys.stdin.readline
n = int(input()) # 4
data = []
q = []
for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(q, (end, start))

for _ in range(n):
    data.append(heapq.heappop(q))

count = 1
x = data[0][0] # 끝나는 시간
for i in range(1, n):
    if data[i][1] >= x:
        count += 1
        x = data[i][0]

print(count)