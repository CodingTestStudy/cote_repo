# b를 a로 만드는 과정을 통해 문제를 해결
a, b = map(int, input().split())
count = 1
while True:
    if b <= a:  # b의 값이 a보다 작거나 같게 되는 경우 중에서
        if b == a:  # b와 a가 같은 경우, 연산 종료
            print(count)
        else:   # 같지 않고 작은 경우, 만들어질 수 없는 값
            print(-1)
        break
    if b % 2 == 0:  # 2로 나누어 떨어진다면, 2로 나눔
        b //= 2
    elif b % 10 == 1:   # 마지막 자릿수가 1이면, 1제거(10으로 나눔)
        b //= 10
    else:   # 위의 두 연산이 불가능하면, a에서 b를 만들 수 없는 경우임
        print(-1)
        break
    count += 1
