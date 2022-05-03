from collections import deque


def solution(A, K):
    if len(A) == 0 or K == 0:
        return A
    time = K % len(A)
    A = deque(A)
    while time:
        time -= 1
        last = A.pop()
        A.appendleft(last)
    return list(A)
