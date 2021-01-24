import sys
import heapq
input = sys.stdin.readline
n = int(input())
data = []
q = []
# 회의시간 (끝나는 시간, 시작 시간) 순서로 끝나는 시간 기준으로 오름차순 정렬
# 가장 빠르게 끝나는 회의실을 찾기 위해
for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(q, (end, start))

for _ in range(n):
    data.append(heapq.heappop(q))

count = 1
x = data[0][0] # 가장 빨리 회의가 끝나는 시간
for i in range(1, n):
    # 회의가 끝나는 시간 다음 가장 빠르게 회의를 시작할 수 있는 시간
    # 회의 시작 시간도 오름차순으로 정렬되어있기 때문에 for문 하나만으로도 빠르게 찾을 수 있다.
    if data[i][1] >= x:
        count += 1
        x = data[i][0]

print(count)