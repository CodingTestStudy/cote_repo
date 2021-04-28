def solution(lottos, win_nums):
    high_count = 0
    low_count = 0
    zero_count = 0

    ranking = [6, 6, 5, 4, 3, 2, 1]
    answer = []
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero_count += 1
            continue

        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                high_count += 1
                low_count += 1
                lottos[i] = 46
                win_nums[j] = 48
                break

    high_count += min(zero_count, len(win_nums) - low_count)
    answer.append(ranking[high_count])
    answer.append(ranking[low_count])

    return answer

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))