from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 모든 경우의 수
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    unique = []
    for comb in combi:
        # comb에 해당하는 데이터 값 삽입
        temp = [tuple([item[c] for c in comb]) for item in relation]

        # 유일성, 데이터가 겹치지 않는지 확인
        if len(set(temp)) == row:
            flag = True
            # 최소성, 부분집합에 속하면 제외
            for u in unique:
                if set(u).issubset(set(comb)):
                    flag = False
                    break
            if flag:
                unique.append(comb)
    return len(unique)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))