import sys
import heapq
N = int(sys.stdin.readline().strip())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
data.sort() # deadline이 짧은 순으로 정렬
q = [] # 힙을 사용하기 위한 리스트
result = 0
for i in range(N, 0, -1):
    # data가 존재하고, data의 최대 deadline이 i 시간보다 같거나 크면
    while data and data[-1][0] >= i:
        # 해당 시간에서 가장 큰 값을 pop으로 빼고, q에 삽입
        heapq.heappush(q, -data.pop()[1])
    if q:
        # q에 저장된 컵라면 개수중 최대 개수를 result에 더해준다
        result -= heapq.heappop(q) # 최대힙
print(result)
