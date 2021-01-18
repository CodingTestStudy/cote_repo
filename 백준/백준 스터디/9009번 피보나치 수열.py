# 9009번 피보나치 수열
import sys
from collections import deque
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
input_data = []
result = deque(deque() for _ in range(n))

for _ in range(n):
    input_data.append(int(input()))

fibo = []
fibo.append(0)
fibo.append(1)
i = 1
while True:
    i += 1
    fibo.append(fibo[i - 1] + fibo[i - 2])
    if max(fibo) >= max(input_data):
        break

print(len(fibo))
print(max(fibo))
count = -1
for value in input_data:
    count += 1
    if value in fibo:
        result[count].appendleft(value)
        continue
    start = bisect_left(fibo, value) - 1
    temp = value # 100
    for i in range(start): # 89의 index 70
        value = temp
        start -= i
        print("START : ", start)
        print("삽입 : ", fibo[start])
        result[count].appendleft(fibo[start])
        value -= fibo[start]
        print("현재 value : ", value)
        x = bisect_left(fibo, value)
        while sum(result[count]) < temp: # 100
            if value - fibo[x] >= 0:
                print("삽입 : ", fibo[x])
                result[count].appendleft(fibo[x])
                value -= fibo[x]
                x = bisect_left(fibo, value)
                print("sum : ", sum(result[count]))
            else:
                print("else 부분")
                x = bisect_left(fibo, value) - 1
        if value == 0:
            break
        elif value < 0:
            for _ in range(len(result[count])):
                result[count].pop()
    print()
    print()

for i in range(n):
    for value in result[i]:
        print(value, end=' ')
    print()
