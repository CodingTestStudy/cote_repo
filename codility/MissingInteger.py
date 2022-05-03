from collections import defaultdict


def solution(A):
    answer_dict = defaultdict(int)
    for a in A:
        if a >= 1:
            answer_dict[a] += 1
    idx = 1
    while True:
        if answer_dict[idx] == 0:
            return idx
        idx += 1
