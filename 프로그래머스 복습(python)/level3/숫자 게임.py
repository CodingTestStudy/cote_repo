def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    # A, B 최대값끼리 비교하면서, B가 더 큰 경우 점수 획득 처리후, B 최대값 삭제 및 갱신
    while A:
        a = A.pop()
        if a < B[-1]:
            answer += 1
            B.pop()
    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))
