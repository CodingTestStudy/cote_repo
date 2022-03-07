def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for index, answer in enumerate(answers):
        if answer == first[index % len(first)]:
            score[0] += 1
        if answer == second[index % len(second)]:
            score[1] += 1
        if answer == third[index % len(third)]:
            score[2] += 1

    result = []
    max_score = max(score)
    for idx, sc in enumerate(score):
        if sc == max_score:
            result.append(idx + 1)
    return result


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))