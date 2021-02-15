N = input() # 이동할 채널
M = int(input()) # 고장난 버튼 개수
if M == 0 and N == '100': print(0) # 고장난 버튼이 없고, 이동 채널이 100인 경우
elif M == 0: # 단순히 고장난 버튼이 없는 경우
    x = len(N) # 이동할 채널의 자릿수 (채널 버튼 눌러서 이동한 경우)
    y = abs(100 - int(N)) # +, -로 이동하는 경우
    print(min(x, y))
elif N == '100': # 고장난 버튼은 있지만, 이동 채널이 100인 경우
    print(0)
else: # 그 외의 경우
    broken = list(map(int, input().split()))
    remote = [i for i in range(10) if i not in broken]

    result = abs(int(N) - 100) # 단순 +, -로 이동하는 경우

    # 모든 경우의 수를 구함
    # 채널은 무한대만큼 존재하고, 이동하고자 하는 채널의 최대 수는 500,000이다.
    # 0에서 500,000까지 이동하는데 +를 최대 500,000번 누를 수 있기 때문에,
    # 반대로 -를 500,000번 눌러서 500,000까지 이동하기 위해서는 무한대의 채널에서
    # 1,000,000까지로 한정지을 수 있다.
    for i in range(1000001):
        data = str(i)
        for j in range(len(data)):
            # 해당 채널의 각 버튼중에서 정상 버튼 리스트에 존재하지 않는 경우
            if int(data[j]) not in remote:
                break
            # 모든 버튼을 검사하고 위에서 걸러지지 않은 경우(모든 버튼이 정상 리스트에 존재하는 경우)
            elif j == len(data) - 1:
                # 기존의 result와 (버튼 입력 횟수 + i에서 입력 채널로 이동하기 위한 +, - 로 이동 횟수) 비교
                result = min(result, len(data) + abs(int(N) - i))

    print(result)

