def solution(price, money, count):
    answer = price * sum([i for i in range(1, count + 1)]) - money
    return answer if answer >= 0 else 0
    # return max(0, price * (count + 1) * count // 2 - money)


print(solution(3, 20, 4))