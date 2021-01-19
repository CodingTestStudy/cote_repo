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

# 피보나치 초기화
fibo = []
fibo.append(0)
fibo.append(1)

# 필요로하는 값까지만 피보나치값 생성(최대값을 기준으로)
i = 1
while True:
    i += 1
    fibo.append(fibo[i - 1] + fibo[i - 2])
    if max(fibo) >= max(input_data):
        break

count = -1
for value in input_data:
    count += 1
    # 입력한 값이 피보나치 값 그 자체인 경우, 해당 값만 결과 리스트에 남기고 다음 단계로
    if value in fibo:
        result[count].appendleft(value)
        continue

    temp = value # 앞으로 value 값을 뺴면서 진행할 것이기 때문에, 임의로 값 저장
    x = bisect_left(fibo, value) - 1 # 입력값보다 작은 값중에서 가장 가까운 값의 index 찾기
    while sum(result[count]) < temp: # 100
        if value - fibo[x] >= 0:
            result[count].appendleft(fibo[x])
            value -= fibo[x]
            x = bisect_left(fibo, value)
        else:
            x = bisect_left(fibo, value) - 1

for i in range(n):
    for value in result[i]:
        print(value, end=' ')
    print()
