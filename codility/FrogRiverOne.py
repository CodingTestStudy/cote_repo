def solution(X, A):
    answer_set = set()
    for i in range(len(A)):
        answer_set.add(A[i])
        if len(answer_set) == X:
            return i
    return -1