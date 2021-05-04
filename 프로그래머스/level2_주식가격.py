# 해당 코드는 O(N^2)의 시간 복잡도
def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        for j in range(i + 1, len(prices)):
            time += 1
            if prices[i] > prices[j]:
                break
        answer.append(time)

    return answer

print(solution([1, 2, 3, 2, 3]))

# 스택을 사용하여 필요한 만큼만 loop 돈다.
# def solution(prices):
#     n = len(prices)
#     answer = [0 for _ in range(n)]
#     stack = [] # 떨어지지 않은 시점 저장된 리스트
#
#     for i in range(n):
#         # i 시점에서 가격이 떨어졌다면
#         while stack and prices[stack[-1]] > prices[i]:
#             top = stack.pop() # 떨어지기 직전 시간
#             answer[top] = i - top
#         stack.append(i)
#
#     while stack:
#         top = stack.pop()
#         answer[top] = n - top - 1
#
#     return answer