import heapq
N = int(input())
K = int(input())
location = sorted(list(map(int, input().split())))

if N <= K: print(0)
else:
    gap = []
    for i in range(len(location) - 1):
        heapq.heappush(gap, -(location[i + 1] - location[i]))   # 시간 복잡도 O(1)
    result = 0
    for i in range(K - 1):
        # heapq를 사용하면, 삽입되어 있는 상태의 순서는 마구잡이이지만
        # heappop()으로 뺄 때는 최소값 우선으로 빠져 나가기 때문에
        # 추가로 정렬연산할 필요X
        # 10줄에 - 붙여서 삽입한거하고 18줄에 - 붙여서 출력하는거는
        # 책에서 힙 배울 때, 최대힙 최소힙 개념 배우면됨
        heapq.heappop(gap)  # 시간 복잡도(1)
    print(-sum(gap))