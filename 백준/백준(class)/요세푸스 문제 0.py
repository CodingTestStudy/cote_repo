from collections import deque
n, k = map(int, input().split())
data = [i for i in range(1, n + 1)]
result = deque()
result.append("<")
location = 0
while data:
    length = len(data)
    location += k - 1
    while location >= length:
        location -= length

    result.append(data[location])
    result.append(", ")
    data.remove(data[location])

result.pop()
result.append(">")
for value in result:
    print(value, end='')



