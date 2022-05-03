def solution(A):
    input_list = [0] * (len(A) + 2)
    for a in A:
        input_list[a] = 1
    for i in range(1, len(A) + 2):
        if input_list[i] == 0:
            return i