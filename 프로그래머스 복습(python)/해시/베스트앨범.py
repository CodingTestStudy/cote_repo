from collections import defaultdict


def solution(genres, plays):
    answer = []
    total = defaultdict(int)
    temp = defaultdict(list)

    for i in range(len(genres)):
        total[genres[i]] += plays[i]
        temp[genres[i]].append([plays[i], i])

    total = sorted(total.items(), key=lambda item: item[1], reverse=True)

    for g, l in total:
        g_list = sorted(temp[g], key=lambda x: (-x[0], x[1]))[:2]

        for i in range(len(g_list)):
            answer.append(g_list[i][1])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))