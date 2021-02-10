# 마을1부터 순서대로 계산하는 것이 아니라,
# 도착순으로 정렬해서, 각 마을에서의 순간 수용량을 갱신해가면서 계산한다.
import sys
N, C = map(int, sys.stdin.readline().strip().split())
M = int(sys.stdin.readline().strip())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
data = sorted(data, key=lambda x: x[1])

village = [C] * (N + 1)
total = 0

def process(s, e, value):
    global total
    for j in range(s, e):
        village[j] -= value
    total += value


for i in range(len(data)):
    start, end = data[i][0], data[i][1]
    box = data[i][2]
    max_capacity = min(village[start:end])

    if max_capacity == 0: continue
    if box <= max_capacity: process(start, end, box)
    else: process(start, end, max_capacity)

print(total)