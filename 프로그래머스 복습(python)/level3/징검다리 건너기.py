def solution(stones, k):
    left, right = 0, 200000000
    while left <= right:
        # mid 만큼의 인원이 건널 수 있는지 확인
        mid = (left + right) // 2
        cnt = 0

        # 가라앉은 디딤돌의 누적 k개를 찾는 과정
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            # 연속하지 않으므로 0으로 초기화
            else:
                cnt = 0

            # 가라앉은 디딤돌이 연속으로 k개 이상이면, mid값이 크다는 의미
            if cnt >= k:
                break

        # 가라앉은 디딤돌이 k개 이상이면, 건너는 인원 줄여보기
        if cnt >= k:
            right = mid - 1
        # 가라앉은 디딤돌이 k개 안된다면, 더 건널수 있다는 의미, 인원 늘리기
        else:
            left = mid + 1
    return left


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
