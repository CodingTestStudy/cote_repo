# 가장 인접한 두 공유기 사이의 거리의 최대값을 구하는 문제
# 가장 인접한 거리를 대상으로 이진 탐색
import sys
n, c = map(int, sys.stdin.readline().split(' '))
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
left = 1
right = data[-1] - data[0]
answer = 0
while left <= right:
    # mid == 가장 인접한 거리 (비교 대상)
    mid = (left + right) // 2
    cur = data[0]
    cnt = 1

    for i in range(1, len(data)):
        # 다음 집하고 mid 이상의 간격 차이가 난다면
        if data[i] >= cur + mid:
            cnt += 1
            cur = data[i]
    # 공유기 설치가 c개 이상 가능하면 간격을 더 늘리기 가능
    if cnt >= c:
        answer = mid
        left = mid + 1
    # 공유기를 c개보다 설치하지 못하면 간격이 너무 크기 때문에 줄여야 함
    else:
        right = mid - 1
print(answer)
