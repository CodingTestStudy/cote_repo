import heapq
import sys
N, M, B = map(int, input().split())
data = []   # 입력받을 데이터의 리스트
q = []  # 시간, 높이 우선순위 큐로 사용할 리스트
height_q = []   # 동시간대에서의 높이들을 비교할 리스트
data_set = set()
for _ in range(N):
    x = list(map(int, sys.stdin.readline().split()))
    data.append(x) # 데이터 입력 받음
    for j in range(M):  # 한 줄 입력받은 데이터의 길이만큼
        data_set.add(x[j])  # set에 삽입(set은 중복 제거)


for value in data_set:  # set에 저장된 높이를 기준으로 잡음
    test_B = B
    time = 0
    for i in range(N):
        for j in range(M):
            # 모든 좌표를 돌면서 set의 value와 비교
            temp = data[i][j]
            if temp > value: # 제거
                x = temp - value # 제거가 필요한 블록 개수
                temp -= x    # 기존의 블록개수에서 필요한만큼 블록 제거
                time += 2 * x   # 제거 블록 개수의 2배시간 소요
                test_B += x     # 제거한만큼 블록 소유 개수 증가
            elif temp < value: # 추가
                x = value - temp # 추가로 필요한 블록 개수
                temp += x    # 기존의 블록개수에서 필요한만큼 블록 추가
                time += x   # 추가 블록 개수만큼 시간 소요
                test_B -= x # 추가한만큼 블록 소유 개수 감소
    if test_B >= 0: # 블록 개수가 0이상인 경우(블록이 모자라지 않았을 경우)
        heapq.heappush(q, (time, value))  # q에 해당 시간과 동일하게 배치된 블록의 개수(높이) 저장


time, height = heapq.heappop(q) # 위에서 구한 시간들 중에서, 가장 짧은 시간과 해당 시간에서의 높이(우선순위 큐)
heapq.heappush(height_q, -height)    # 시간이 동일한 경우, 높은 높이의 블록 개수를 출력하기 위해 높이 리스트에 저장
while q:
    next_time, next_height = heapq.heappop(q)
    if time != next_time: break # 위에서 구한 time(가장 짧은 시간)과 동일한 시간이 존재하지 않으면 break
    else: heapq.heappush(height_q, -next_height)    # 복수개의 가장 짧은 시간이 존재한다면, 해당 시간에서의 높이를 높이 리스트에 삽입

print(time, -heapq.heappop(height_q))   # 시간은 이미 위에서 구했고, 높이 리스트에서 가장 큰값을 pop
