N = int(input()) # 1 <= N <= 1,000
# 1억 연산 1초 -> O(n^3) 알고리즘까지 아마 가능
A = list(map(int, input().split()))
dp = [1 for _ in range(N)] # 존재 자체만으로 길이 1
max_value = -1
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + 1, dp[i])
            
print(max(dp))

# N = int(input())
# A = list(map(int, input().split()))
# result = [A[0]]
# 
# for i in range(1, N):
#     if result[-1] < A[i]:
#         result.append(A[i])
#     else:
#         if A[i] in result:
#             continue
# 
#         for j in range(len(result)):
#             if result[j] > A[i]:
#                 result[j] = A[i]
#                 break
# print(len(result))
