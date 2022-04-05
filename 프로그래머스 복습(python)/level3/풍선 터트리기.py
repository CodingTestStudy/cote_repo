def solution(a):
    answer = [False for _ in range(len(a))]
    left, right = 1e12, 1e12

    # 현재 위치에서 왼쪽 전체 혹은 오른쪽 전체에 현재 값보다 큰 경우만 존재하면
    # 마지막까지 남을 수 있음
    for i in range(len(a)):
        if a[i] < left:
            left = a[i]
            answer[i] = True
        if a[-1 - i] < right:
            right = a[-1 - i]
            answer[-1 - i] = True

    return sum(answer)


print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))


# more simple code
# def solution(a):
#     answer = 1
#     min_value = min(a)
#     # 앞뒤 반복을 위해 반복문 2번
#     for _ in range(2):
#         m = a[0]
#         idx = 1
#         while m != min_value:
#             if m >= a[idx]:
#                 m = a[idx]
#                 answer += 1
#             idx += 1
#         a.reverse()
#     return answer