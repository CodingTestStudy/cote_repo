import sys
import heapq
N = int(input())
data = []
for _ in range(N):
    heapq.heappush(data, int(sys.stdin.readline()))

result = 0
while len(data) >= 2:
    # 갱신된 카드 리스트에서 가장 작은 2개 호출
    data1, data2 = heapq.heappop(data), heapq.heappop(data)
    data3 = data1 + data2
    heapq.heappush(data, data3)
    # 카드 리스트에 합친 묶음으로 갱신
print(result)