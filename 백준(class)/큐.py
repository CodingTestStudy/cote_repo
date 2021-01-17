from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
result = deque()
for _ in range(n):
    pro = list(input().split())
    if pro[0] == 'push':
        result.append(pro[1])
    elif pro[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.popleft())
    elif pro[0] == 'size':
        print(len(result))
    elif pro[0] == 'empty':
        if len(result) == 0: print(1)
        else: print(0)
    elif pro[0] == 'front':
        if len(result) == 0: print(-1)
        else:
            x = result.popleft()
            print(x)
            result.appendleft(x)
    else:
        if len(result) == 0: print(-1)
        else:
            x = result.pop()
            print(x)
            result.append(x)