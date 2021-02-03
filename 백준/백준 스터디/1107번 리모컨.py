N = input() # 이동할 채널
M = int(input()) # 고장난 버튼 개수
if M == 0 and N == '100': print(0)
elif M == 0:
    x = len(N)
    y = abs(100 - int(N))
    print(min(x, y))
elif N == '100':
    print(0)
else:
    broken = list(map(int, input().split()))
    remote = [i for i in range(10) if i not in broken]

    result = abs(int(N) - 100)


    for i in range(1000001):
        data = str(i)
        for j in range(len(data)):
            if int(data[j]) not in remote:
                break
            elif j == len(data) - 1:
                result = min(result, abs(int(N) - i) + len(data))

    print(result)

