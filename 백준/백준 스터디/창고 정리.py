import sys
import heapq
serial_num = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    data = sys.stdin.readline().strip()
    num = 0
    for value in data:
        if 48 <= ord(value) <= 57:
            num += int(value)
    heapq.heappush(serial_num, (len(data), num, data))

while serial_num:
    length, num, data = heapq.heappop(serial_num)
    print(data)
