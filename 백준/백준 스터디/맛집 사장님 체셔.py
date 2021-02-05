import sys
from collections import deque
N = int(input())
custom_list = []
for _ in range(N):
    start, wait = map(int, sys.stdin.readline().strip().split())
    custom_list.append((start, wait))

c_list = deque(sorted(custom_list))
time = 0

for i in range(N):
    x, y = c_list.popleft()
    if x > time:
        time = 0
        time += x + y
    else:
        time += y

print(time)

