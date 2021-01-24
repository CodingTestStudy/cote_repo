# dictionary 사용, 힙 사용
import heapq
N = int(input())
data = []
for _ in range(N):
    data.append(input())

data_dict = dict()
for word in data:
    length = len(word) - 1
    for s in word:
        if s in data_dict:
            data_dict[s] += pow(10, length)
        else:
            data_dict[s] = pow(10, length)
        length -= 1

q = []
for value in data_dict.values():
    heapq.heappush(q, -value)

result = 0
start = 9
while q:
    result += -heapq.heappop(q) * start
    start -= 1

print(result)