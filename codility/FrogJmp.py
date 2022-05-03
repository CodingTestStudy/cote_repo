def solution(X, Y, D):
    term = Y - X
    if term % D == 0:
        return term // D
    return term // D + 1
