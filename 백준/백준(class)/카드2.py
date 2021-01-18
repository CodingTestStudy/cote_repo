from collections import deque
n = int(input())
data = deque()
for i in range(1, n + 1): data.append(i)

while len(data) != 1:
    data.popleft()
    x = data.popleft()
    data.append(x)

print(data.pop())