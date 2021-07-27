def solution(N, number):
    answer = -1
    dp = []

    # i는 숫자 사용횟수
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(0, i - 1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)

                    # 나눌 수 있는 경우, 몫도 저장
                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            answer = i
            break

        # 다음 계산을 할 때, 사용할 수 있는 숫자들
        dp.append(numbers)

    return answer

print(solution(5, 12))
print(solution(2, 11))