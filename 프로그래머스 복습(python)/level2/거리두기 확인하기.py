from collections import defaultdict


def solution(places):
    # 맨허튼 거리 (r1, c1), (r2, c2)
    # |r1-r2| + |c1-c2|
    answer = []
    for place in places:
        people = []
        for r in range(len(place)):
            for c in range(len(place[0])):
                if place[r][c] == 'P':
                    people.append([r, c])
        target = defaultdict(list)
        for i in range(len(people)):
            for j in range(len(people)):
                if i != j:
                    r, c = people[i][0], people[i][1]
                    nr, nc = people[j][0], people[j][1]
                    # 맨허튼 거리가 2 이하인 people 위치 저장
                    if abs(nr - r) + abs(nc - c) <= 2:
                        target[(r, c)].append(people[j])

        # 맨허튼 거리가 2 이하인 poeple 사이에 벽의 유무 확인
        is_exist_bar = True
        for people in target.keys():
            r, c = people[0], people[1]
            for n_people in target[people]:
                new_r, new_c = n_people[0], n_people[1]
                if new_r == r:
                    if place[r][(c + new_c) // 2] != 'X':
                        is_exist_bar = False
                        break
                elif new_c == c:
                    if place[(r + new_r) // 2][c] != 'X':
                        is_exist_bar = False
                        break
                else:
                    if place[r][new_c] != 'X' or place[new_r][c] != 'X':
                        is_exist_bar = False

            # 벽이 없는 경우 발견하면 반복문 종료
            if not is_exist_bar:
                break
        if is_exist_bar:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
