import sys

input = sys.stdin.readline

k, n, = map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))

line.sort()
answer = 0
left, right = 0, 2 ** 31
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for l in line:
        cnt += l // mid
    if cnt >= n:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
