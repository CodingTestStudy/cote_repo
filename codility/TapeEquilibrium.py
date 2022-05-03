def solution(A):
    left, right = 0, sum(A)
    answer_set = set()
    for i in range(len(A) - 1):
        left += A[i]
        right -= A[i]
        answer_set.add(abs(left - right))
    return min(answer_set)