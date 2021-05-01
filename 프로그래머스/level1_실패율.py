def solution(N, stages):
    answer = []
    survive = len(stages)
    for i in range(1, N + 1):
        if stages.count(i):
            answer.append([stages.count(i) / survive, i])
        else:
            answer.append([0, i])
        survive -= stages.count(i)

    return [i[1] for i in sorted(answer, key=lambda x : (x[0], -x[1]), reverse=True)]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))