def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    # 1. 맨 앞 스티커 뗀 경우
    dp1 = [0 for _ in range(len(sticker))]
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
    first_case_value = max(dp1)

    # 2. 맨 앞 스티커 안 뗀 경우
    dp2 = [0 for _ in range(len(sticker))]
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])
    second_case_value = max(dp2)

    return max(first_case_value, second_case_value)


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
