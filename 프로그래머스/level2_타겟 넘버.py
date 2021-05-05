from collections import deque, Counter

def solution(numbers, target):
    n = deque(numbers)
    x = n.popleft()
    sum_list = deque([x, -x])
    while n:
        y = n.popleft()
        for i in range(len(sum_list)):
            z = sum_list.popleft()
            sum_list.append(z + y)
            sum_list.append(z - y)
    return Counter(sum_list)[target]

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))


# DFS 사용 코드
# answer = 0
# def DFS(idx, numbers, target, value):
#     global answer
#     N = len(numbers)
#     if(idx== N and target == value):
#         answer += 1
#         return
#     if(idx == N):
#         return
#
#     DFS(idx+1,numbers,target,value+numbers[idx])
#     DFS(idx+1,numbers,target,value-numbers[idx])
# def solution(numbers, target):
#     global answer
#     DFS(0,numbers,target,0)
#     return answer


# 단순 재귀 코드
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


# itertools, product 사용

# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)