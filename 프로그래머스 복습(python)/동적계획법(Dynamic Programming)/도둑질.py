import copy


def solution(money):
    # 첫 집을 터는 경우
    first_money = copy.deepcopy(money)
    first_money[2] += first_money[0]
    # 첫 집을 안 터는 경우
    second_money = copy.deepcopy(money)
    second_money[0] = 0

    for i in range(3, len(money)):
        first_money[i] += max(first_money[i - 3], first_money[i - 2])
        second_money[i] += max(second_money[i - 3], second_money[i - 2])
    max_first_money = max(first_money[len(money) - 3], first_money[len(money) - 2])
    max_second_money = max(second_money[len(money) - 2], second_money[len(money) - 1])
    return max(max_first_money, max_second_money)


print(solution([1, 2, 3, 1]))
