# bfs
from collections import deque


def bfs(n, info):
    result = []
    q = deque([(0, [0 for _ in range(11)])])
    max_diff = 0

    while q:
        score, arrow = q.popleft()

        # 화살을 다 쏜 경우
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                # 둘 중 하나 이상 맞춘 경우
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:
                diff = lion - apeach
                # 갱신할 필요 없는 경우
                if max_diff > diff:
                    continue
                # 갱신 해야 하는 경우
                if max_diff < diff:
                    max_diff = diff
                    result.clear()
                # 최대 점수차 화살 저장
                result.append(arrow)
        # 화살을 더 쏜 경우
        elif sum(arrow) > n:
            continue
        # 마지막 과녁인 경우(나머지 화살 다 쏘기)
        elif score == 10:
            temp = arrow.copy()
            temp[score] = n - sum(temp)
            q.append((-1, temp))
        # score 에 화살 쏘기
        else:
            # score 에 1발 더 맞춘 경우
            temp = arrow.copy()
            temp[score] = info[score] + 1

            # score + 1 을 삽입해서 arrow의 총합이 n이 넘는 경우가 생길 수 있음
            # 위 조건문 elif sum(arrow) > n 필요
            q.append((score + 1, temp))

            # score 아예 안 맞춘 경우
            temp2 = arrow.copy()
            temp2[score] = 0
            q.append((score + 1, temp2))
    return result


def solution(n, info):
    answer = bfs(n, info)
    if not answer:
        return [-1]
    return answer[-1]

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))


# # 모든 경우의 수 순회(비효율적)
# from collections import Counter
# from itertools import combinations_with_replacement
#
#
# def solution(n, info):
#     max_diff, max_cnt = 0, dict()
#
#     # 중복 조합
#     for comb in combinations_with_replacement(range(11), n):
#         print(f"comb = {comb}")
#         cnt = Counter(comb)
#         print(f"cnt = {cnt}")
#         lion, apeach = 0, 0
#         for i in range(1, 11):
#             if info[10 - i] < cnt[i]:
#                 lion += i
#             elif info[10 - i] > 0:
#                 apeach += i
#
#         diff = lion - apeach
#         if diff > max_diff:
#             max_cnt = cnt
#             max_diff = diff
#
#     if max_diff > 0:
#         answer = [0] * 11
#         for score in max_cnt:
#             answer[10 - score] = max_cnt[score]
#         return answer
#     else:
#         return [-1]
