from collections import deque
n = int(input())
data = []
result = []
for _ in range(n):
    data.append(input())

def solution(data):
    count = 0
    for i in range(len(data)):
        if data[i] == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return "NO"
    if count == 0: return "YES"
    else: return "NO"

for value in data:
    print(solution(value))