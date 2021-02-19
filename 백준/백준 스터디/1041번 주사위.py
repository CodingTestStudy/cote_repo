N = int(input())
dice = list(map(int, input().split()))
sum_list = []
if N == 1: print(sum(dice) - max(dice))
else:
    for _ in range(3):
        min_index = 7
        min_value = 51
        for i in range(len(dice)):
            if dice[i] < min_value:
                min_index = i
                min_value = dice[i]
        first = min_value
        first_min_index = min_index
        ignore_index = 5 - min_index

        min_index = 7
        min_value = 51
        for j in range(len(dice)):
            if j == first_min_index or j == ignore_index: continue
            if dice[j] < min_value:
                min_index = j
                min_value = dice[j]
        second = min_value
        second_min_index = min_index
        ignore_index_2 = 5 - second_min_index
        min_value = 51
        for k in range(len(dice)):
            if first_min_index == k or second_min_index == k or k == ignore_index or k == ignore_index_2: continue
            if dice[k] < min_value:
                min_value = dice[k]
        third = min_value

        plane1 = N * N * first
        plane2 = 2 * N * second + (N - 2) * N * first
        plane3 = (N - 2) * (N - 2) * first + (N - 2) * 4 * second + 4 * third
        sum_value = 2 * plane1 + 2 * plane2 + plane3
        sum_list.append(sum_value)
        dice[first_min_index] = 1e9

    print(min(sum_list))
