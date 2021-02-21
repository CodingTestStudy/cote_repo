N = int(input())
dice = list(map(int, input().split()))
# N이 1인 경우, 단순 정육면체 형태이므로, 가장 큰 수를 바닥에 배치하고
# 나머지 값들을 더한다.
if N == 1:
    print(sum(dice) - max(dice))
# 그 외의 경우
# 주사위의 3면에 배치할 수 있는 가장 작은 값 3개를 선정한다.
# 큐브에 특성에 따라서, 선정된 값과 마주보는 면은 쓰일 수 없으므로, 배제시키며 진행
else:
    min_index = 7
    min_value = 51
    # 가장 작은 값을 가진 면 찾기
    for i in range(len(dice)):
        if dice[i] < min_value:
            min_index = i
            min_value = dice[i]
    first = min_value # 가장 작은 값
    first_min_index = min_index # 가장 작은 값을 가진 면의 index
    ignore_index = 5 - min_index # 그 면의 반대면 index

    min_index = 7
    min_value = 51
    # 2번째로 작은 값을 가진 면 찾기
    for j in range(len(dice)):
        # 기존에 선정된 가장 작은 면과 그 면의 반대면은 후보에서 제오
        if j == first_min_index or j == ignore_index: continue
        if dice[j] < min_value:
            min_index = j
            min_value = dice[j]
    second = min_value # 2번째로 작은 값
    second_min_index = min_index # 2번째로 작은 면의 index
    ignore_index_2 = 5 - second_min_index # 그 면의 반대면

    min_value = 51
    # 3번째로 작은 값을 가진 면 찾기
    for k in range(len(dice)):
        # 위에 해당하는 면들 모두 제외
        if first_min_index == k or second_min_index == k or k == ignore_index or k == ignore_index_2: continue
        if dice[k] < min_value:
            min_value = dice[k]
    third = min_value # 3번째로 작은 값

    plane1 = N * N * first
    plane2 = 2 * N * second + (N - 2) * N * first
    plane3 = (N - 2) * (N - 2) * first + (N - 2) * 4 * second + 4 * third
    sum_value = 2 * plane1 + 2 * plane2 + plane3
    print(sum_value)
