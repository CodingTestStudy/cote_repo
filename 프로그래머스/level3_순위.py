# 더 가독성 좋은 코드
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set),
    for winner, looser in results:
        win[winner].add(looser)
        lose[looser].add(winner)

    for i in range(1, n + 1):
        for winner in lose[i]:
            win[winner].update(win[i])
        for looser in win[i]:
            lose[looser].update(lose[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# 그래프를 이용한 코드
def solution(n, results):
    total = [['?' for i in range(n)] for j in range(n)]

    for i in range(n):
        total[i][i] = 'SELF'

    for result in results:
        total[result[0]-1][result[1]-1] = 'WIN'
        total[result[1]-1][result[0]-1] = 'LOSE'

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == 'WIN' and total[k][j] == 'WIN':
                    total[i][j] = 'WIN'
                elif total[i][k] == 'LOSE' and total[k][j] == 'LOSE':
                    total[i][j] = 'LOSE'

    answer = 0

    for i in total:
        if '?' not in i:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# def solution(n, results):
#     win, lose = {}, {}
#     for i in range(1, n + 1):
#         win[i], lose[i] = set(), set()
#
#     for i in range(1, n + 1):
#         for winner, looser in results:
#             # i번째 선수 승리한 경우
#             if winner == i:
#                 win[i].add(looser)
#             # i번째 선수 패배한 경우
#             if looser == i:
#                 lose[i].add(winner)
#
#         # i 번째 선수를 이긴 사람들
#         # i에게 진 사람들을 반드시 이김
#         for winner in lose[i]:
#             win[winner].update(win[i])
#
#         # i 번째 선수가 이긴 사람들
#         # i를 이긴 사람들에게 반드시 짐
#         for looser in win[i]:
#             lose[looser].update(lose[i])
#
#     answer = 0
#     for i in range(1, n + 1):
#         if len(win[i]) + len(lose[i]) == n - 1:
#             answer += 1
#     return answer