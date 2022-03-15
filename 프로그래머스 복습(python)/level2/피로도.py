from itertools import permutations


def solution(k, dungeons):
    answer = -1
    per = permutations([i for i in range(len(dungeons))], len(dungeons))
    for pe in per:
        my_k = k
        cnt = 0
        for p in pe:
            need, minus = dungeons[p][0], dungeons[p][1]
            if my_k >= need:
                my_k -= minus
                cnt += 1
            else:
                break
        answer = max(answer, cnt)

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
