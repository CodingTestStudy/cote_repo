import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
answer = []
while T != 0:
    T -= 1
    p = list(input().strip())
    n = int(input())
    x = deque(input().strip('[]\n').split(','))

    flag = True
    is_error = False
    for order in p:
        if order == 'R':
            flag = not flag
        else:
            if len(x) == 0 or x[0] == '':
                answer.append("error")
                is_error = True
                break
            if flag:
                x.popleft()
            else:
                x.pop()

    if not is_error:
        if len(x) > 0 and not flag:
            x.reverse()
        answer.append(x)

for ans in answer:
    if ans == 'error':
        print(ans)
    else:
        print('[', end='')
        for i in range(len(ans)):
            if i == len(ans) - 1:
                print(ans[i], end='')
            else:
                print(ans[i], end=',')

        print(']')