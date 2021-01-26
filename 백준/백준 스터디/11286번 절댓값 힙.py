import sys
import heapq
N = int(input())
q = []
for _ in range(N):
    data = int(sys.stdin.readline().rstrip())
    if data == 0 and len(q) == 0: # 입력된 데이터가 0이면서, 해당 리스트가 비어있다면
        print(0) # 0 출력
    elif data == 0: # 0을 입력받고, 리스트 내에 데이터가 존재한다면
        print(heapq.heappop(q)[1]) # 최솟값 데이터 출력
    else:
        heapq.heappush(q, (abs(data), data)) # 입력된 데이터 삽입
        # 첫 번째 데이터 값을 절댓값으로 삽입하여, heappop 으로 값을 추출할 때, 절댓값 크기 순으로 출력가능함