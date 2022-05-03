from collections import defaultdict
def solution(A):
    num_dict = defaultdict(int)
    for a in A:
        num_dict[a] += 1
    for num in num_dict.keys():
        if num_dict[num] % 2 == 1:
            return num