import sys
input = sys.stdin.readline

N, H = map(int, input().split())
suk = [0] * (H + 1)
jong = [0] * (H + 1)

for i in range(N):
    hh = int(input())
    if i % 2 == 0:
        suk[hh] += 1
    else:
        jong[hh] += 1

for i in range(H-1, 0, -1):
    suk[i] += suk[i + 1]
    jong[i] += jong[i + 1]

answer = N + 1
answer_count = 0
for i in range(1, H + 1):
    if answer > (suk[i] + jong[H - i + 1]):
        answer = suk[i] + jong[H - i + 1]
        answer_count = 1
    elif answer == (suk[i] + jong[H - i + 1]):
        answer_count += 1

print(answer, answer_count)

# 시간초과
# N, H = map(int, input().split())
# visited = [0] * (H + 1)
# for i in range(1, N + 1):
#     hh = int(input())
#     if i % 2 == 1:
#         for j in range(1, hh + 1):
#             visited[j] += 1
#     else:
#         for j in range(H + 1 - hh, H + 1):
#             visited[j] += 1
#
# min_count = 0
# result = N + 1
#
# for i in range(1, H + 1):
#     if visited[i] < result:
#         result = visited[i]
#         min_count = 1
#     elif visited[i] == result:
#         min_count += 1
#
# print(result, min_count)