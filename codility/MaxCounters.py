def solution(N, A):
    answer = [0] * (N + 1)
    max_value = 0
    value = 0
    for i in range(len(A)):
        if 1 <= A[i] <= N:
            if answer[A[i]] < max_value:
                answer[A[i]] = max_value
            answer[A[i]] += 1
            value = max(value, answer[A[i]])
        else:
            max_value = value
    for i in range(N + 1):
        if answer[i] < max_value:
            answer[i] = max_value
    return answer[1:]
