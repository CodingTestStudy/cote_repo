def solution(A):
    answer, temp = 0, 0
    for i in range(len(A) - 1, -1, -1):
        if A[i] == 1:
            temp += 1
        else:
            answer += temp
        A[i] = temp
    if answer > 1000000000:
        return -1
    return answer
