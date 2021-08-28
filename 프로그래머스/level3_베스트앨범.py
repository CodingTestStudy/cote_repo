from collections import defaultdict

def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(int)
    genres_index = defaultdict(list)
    for i in range(len(genres)):
        genres_dict[genres[i]] += plays[i]
        genres_index[genres[i]].append((plays[i], i))

    genres_dict = sorted(genres_dict.items(), key=lambda x: x[1], reverse=True)

    for index in genres_index:
        genres_index[index] = sorted(genres_index[index], key=lambda x:x[0], reverse=True)[:2]

    for i in range(len(genres_dict)):
        name, total = genres_dict[i]
        for tot, index in genres_index[name]:
            answer.append(index)
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
