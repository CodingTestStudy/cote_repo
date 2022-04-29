import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
T = int(input())
calc = ['+', '-', ' ']
while T:
    result = []
    result2 = []
    answer = []

    T -= 1
    N = int(input())
    nums = [i for i in range(1, N + 1)]
    q = deque()
    q.append((["1"], 1))
    while q:
        temp, cnt = q.popleft()

        if cnt == N:
            result.append(temp)
            continue
        for cal in calc:
            test = []
            test.extend(temp)
            test.append(cal)
            test.append(str(cnt + 1))
            q.append((test, cnt + 1))

    result2 = deepcopy(result)

    for idx, res in enumerate(result):
        for i in range(len(res)):
            if res[i] == ' ':
                res[i] = res[i - 1] + res[i + 1]
                res[i - 1], res[i + 1] = '', ''
        data = eval(''.join(res))

        if data == 0:
            answer.append(result2[idx])

    answer.sort()
    for ans in answer:
        print(''.join(ans))
    print()
