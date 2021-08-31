from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for k in course:  # k : 뽑는 갯수
        temp = []
        for menu in orders:
            for m in combinations(menu, k):
                result = ''.join(sorted(m)) # 순서가 달라도 똑같이 취급해야 하기 때문에 정렬한 처리
                temp.append(result)
        # 조합된 문자들 중 개수가 가장 많은 순으로 (문자, 개수)
        sorted_temp = Counter(temp).most_common()

        # cnt 가 동일한 조합이 존재할 수 있기 때문에, 앞부분만 뽑는 것이 아닌, 조건문을 달아서 answer 에 삽입
        answer += [name for name, cnt in sorted_temp if cnt > 1 and cnt == sorted_temp[0][1]]
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
