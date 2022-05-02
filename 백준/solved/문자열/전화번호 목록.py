import sys

input = sys.stdin.readline
T = int(input())
while T:
    T -= 1
    N = int(input())
    numbers = [input().strip() for _ in range(N)]
    numbers.sort()
    flag = True
    for i in range(len(numbers) - 1):
        target = numbers[i]
        if target == numbers[i + 1][:len(target)]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
