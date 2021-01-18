import heapq
n = int(input())
array = []
result = []
for i in range(n):
    keep = True
    data = input()
    length = len(data)
    heapq.heappush(array, (length, data))
    
while array:
    x = heapq.heappop(array)
    if not x[1] in result:
        result.append(x[1])
        print(x[1])


