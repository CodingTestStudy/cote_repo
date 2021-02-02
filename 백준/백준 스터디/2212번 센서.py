# sort()를 사용하지 않고, heapq가 사용이 더 효율적일 줄 알았는데,
# heapq를 for문으로 2번이나 사용하기 떄문에, 오히려 손해
import heapq
N = int(input()) # 센서 개수
K = int(input()) # 집중국 개수
location = sorted(list(map(int, input().split()))) # 센서 좌표 입력 및 정렬

if N <= K: print(0) # 집중국 개수가 센서보다 많다면
else:
    gap = []
    for i in range(len(location) - 1): # 모든 센서 좌표에 대해서
        heapq.heappush(gap, -(location[i + 1] - location[i])) # 각 센서 좌표 간의 거리를 최대힙으로 삽입
    result = 0
    for i in range(K - 1):
        heapq.heappop(gap) # 절댓값 최대 거리 차이를 뺀다
    print(-sum(gap)) # 남은 거리들 더한다. (최대 힙이기 때문에 다시 - 를 붙여서 더한다.)

# # 기존의 나의 코드는 heapq를 사용
# # heapq를 사용해서 돌려보니 오히려 시간복잡도상 조금 손해
# N = int(input())
# K = int(input())
# data = list(map(int, input().split()))
# data.sort()
# 
# if N == 1 and K == 1:  # 센서 개수와 집중국이 둘다 1개라면
#     print(1)
# elif N == 1:  # 센서 1개, 집중국 여러개라면
#     print(0)  # 센서가 어디에 있든 적어도 하나의 집중국과 통신이 가능하기 때문에(어차피 최소값 구하는거기 때문에)
# elif K == 1:  # 집중국이 1개, 센서 여러개라면, 모든 센서가 최소한 적어도 하나의 집중국과 총신이 가능해야 하기 때문에
#     print(data[-1] - data[0])  # 센서가 가장 먼곳에서 가장 가까운 곳의 차이가 수신 가능 영역 길이
# else:
#     # 센서간의 거리 차이를 모아둔 리스트
#     diff_list = [data[i + 1] - data[i] for i in range(len(data) - 1)]
#     diff_list.sort()  # 거리가 짧은 것들을 선출해야 하므로, 오름차순 정렬
#     # 마을 분할하는 느낌으로 도로 자르는 개념와 비슷
#     # 1개의 마을을 2개로 분할하기 위해, 연결된 도로1개를 자르듯
#     for _ in range(K - 1):
#         diff_list.pop()
#     print(sum(diff_list))
