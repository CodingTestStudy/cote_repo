import sys
input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    pro = list(input().split())
    if pro[0] == 'push':
        result.append(pro[1])

    elif pro[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())

    elif pro[0] == 'top':
        if len(result) == 0:
            print(-1)
        else:
            x = result.pop()
            print(x)
            result.append(x)
    elif pro[0] == 'size':
        print(len(result))
    else:
        if len(result) == 0: print(1)
        else: print(0)

