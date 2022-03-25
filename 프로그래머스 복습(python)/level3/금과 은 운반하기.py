# 이분 탐색
def solution(a, b, g, s, w, t):
    # 최대 시간: (도시가 갖을 수 있는 금, 은 무게) * (최대 소요 시간) * (최소 무게)
    # (금, 은), (왕복) 조건 떄문에 2씩 곱함
    answer = (2 * 1e9) * (2 * 1e5) * 1
    start = 0
    end = (2 * 1e9) * (2 * 1e5) * 1
    while start <= end:
        mid = (start + end) // 2
        gold, silver, total = 0, 0, 0

        for i in range(len(g)):
            now_gold = g[i]
            now_silver = s[i]
            now_weight = w[i]
            now_time = t[i]

            # mid에는 마지막 편도 시간도 포함되어 있음. mid에서 편도시간 제거 후 계산, 그리고 편도 횟수 증가
            move_cnt = (mid - now_time) // (now_time * 2) + 1

            gold += min(now_gold, move_cnt * now_weight)
            silver += min(now_silver, move_cnt * now_weight)
            total += min(now_gold + now_silver, move_cnt * now_weight)

        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
