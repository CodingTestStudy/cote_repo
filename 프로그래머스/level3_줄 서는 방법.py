import math
def solution(n, k):
    answer = []
    num_list = [i for i in range(1, n + 1)]
    while n != 0:
        temp = math.factorial(n - 1)
        answer.append(num_list.pop((k - 1) // temp))
        # idx = k // temp
        # k = k % temp
        # if k == 0:
        #     answer.append(num_list.pop(idx - 1))
        # else:
        #     answer.append(num_list.pop(idx))
        n -= 1
        k = k % temp
    return answer

print(solution(3, 5))
# 시간 초과
# from itertools import permutations
# def solution(n, k):
#     answer = [i for i in range(1, n + 1)]
#     answer_list = list(permutations(answer, n))
#     return answer_list[k-1]