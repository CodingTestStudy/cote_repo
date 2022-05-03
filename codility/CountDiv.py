def solution(A, B, K):
    start = A // K if A % K != 0 else A // K - 1
    end = B // K
    return end - start
