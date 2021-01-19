import sys, heapq
input = sys.stdin.readline
n = int(input())
q = []
data = []

for _ in range(n):
    input_data = int(input())
    heapq.heappush(q, -input_data)

for _ in range(n):
    data.append(-heapq.heappop(q))

print(data)
i = 0
result1 = 0


while i < n:
    if i + 1 < n: # 다음 값이 존재하면서
        if data[i] == data[i + 1] and data[i + 1] > 0: # 서로 같은 경우(양수에 한해서)
            result1 += data[i] + data[i + 1]
        elif data[i + 1] > 1 or data[i] <= 0: # (양, 양), (음, 음), (0, 음)
            result1 += data[i] * data[i + 1]
        else: # 그 외의 경우
            result1 += data[i] + data[i + 1]
        i += 2
    else:
        result1 += data[i]
        break

i = n - 1
result2 = 0
while i >= 0:
    if i - 1 >= 0: # 다음 값이 존재하면서
        if data[i] == data[i - 1] and data[i] > 0:
            result2 += data[i] + data[i - 1]
        elif data[i] > 1 or data[i - 1] <= 0:
            result2 += data[i] * data[i - 1]
        else:
            result2 += data[i] + data[i - 1]
        i -= 2
    else:
        result2 += data[i]
        break

print(max(result1, result2))