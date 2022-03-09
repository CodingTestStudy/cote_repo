# 못 푼문제
def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(i - 1):
            for x in dp[j]:
                for y in dp[-j - 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    if y != 0:
                        numbers.add(x // y)
        if number in numbers:
            answer = i
            break
        print(f"{N}을 {i}번 사용")
        dp.append(numbers)
        print(dp)

    return answer

print(solution(5, 12))
print(solution(2, 11))
