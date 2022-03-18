# 이분탐색
def solution(n, times):
    # right = 가장 긴 심사기간에 모두 김사받는 경우(최악의 경우)
    left, right = 1, max(times) * n
    while left < right:

        # 총 소요시간
        mid = (left + right) // 2

        # 심사가능 인원
        total = 0
        for time in times:
            # 총 소요시간에서 각 time에 심사 가능 인원 추가
            total += mid // time

        # 심사 가능 인원이 n명 이상이면 총 소요시간 줄이기
        if total >= n:
            right = mid
        # 심사 가능 인원이 n명이 안되면 총 소요시간 늘리기
        else:
            left = mid + 1
    answer = left
    return answer


print(solution(6, [7, 10]))
