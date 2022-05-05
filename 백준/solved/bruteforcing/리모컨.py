N = int(input())
M = int(input())
# 시작, 도착 번호가 같은 경우
if N == 100:
    print(0)
    exit()
# 고장난 버튼이 없는 경우
if M == 0:
    answer = min(abs(100 - N), len(str(N)))
    print(answer)
    exit()

answer = abs(N - 100)
button = list(map(int, input().split()))
possible = [str(i) for i in range(10) if i not in button]

for target in range(1000001):
    flag = True
    for tar in str(target):
        if tar not in possible:
            flag = False
            break
    if flag:
        answer = min(answer, len(str(target)) + abs(target - N))
print(answer)
