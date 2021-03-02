import sys
import heapq

N, K = map(int, sys.stdin.readline().strip().split())
gem, bag, result = [], [], []

for _ in range(N):
    M, V = map(int, sys.stdin.readline().strip().split())
    gem.append((M, V))
gem.sort(reverse=True) # 무게가 가벼운 순서로 정렬

for _ in range(K):
    C = int(sys.stdin.readline().strip())
    bag.append(C)
bag.sort() # 무게가 가벼운 순서대로 정렬

temp = [] # 해당 가방에 넣을 수 있는 보석들을 저장하는 리스트
# 무게가 가벼운 가방부터, 넣을 수 있는 보석을 temp에 누적함.
while bag: # 가방을 다 쓸 때까지
    bag_weight = heapq.heappop(bag) # 가방의 무게
    # 보석이 존재하고, 가장 가벼운 보석이 가방보다 가볍다면
    while gem and gem[-1][0] <= bag_weight:
        m, v = gem.pop() # 해당 보석정보
        heapq.heappush(temp, -v) # 최대힙을 사용
    if temp: # 보석이 쌓여있으면
        # 그 중 가장 큰 보석의 가격을 result 리스트에 삽입한다. (최대힙)
        # temp에는 해당 가방에 넣을 수 있는 보석들로만 저장되어 있기 때문
        result.append(-heapq.heappop(temp))

print(sum(result)) # 가방에 넣은 보석들의 가격의 합을 출력
