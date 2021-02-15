import sys
N, C = map(int, sys.stdin.readline().strip().split())
M = int(sys.stdin.readline().strip())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
data = sorted(data, key=lambda x: x[1]) # 도착 지점을 기준으로 오름차순 정렬

village = [C] * (N + 1) # 모든 마을에 대해 최대 수용량으로 초기화
total = 0 # 최종 최대 배송 박스 수

def process(s, e, value):
    global total
    # 출발지점부터 도착지점 전까지의 마을들에 대해서
    # 각 지점에서의 수용량에서 박스 개수를 빼준다.
    for j in range(s, e):
        village[j] -= value
    total += value # 배송 가능 박스 수를 더해준다.


for i in range(len(data)):
    start, end = data[i][0], data[i][1] # 출발지점, 도착지점
    box = data[i][2] # 배송할 박스
    # 출발지점부터 도착지점 전까지 수용할 수 있는 박스 개수
    max_capacity = min(village[start:end])
    # 수용가능한 박스 개수가 0이라면, continue
    if max_capacity == 0: continue

    # 현재 박스 개수가 수용 가능한 박스 개수 이하인 경우
    if box <= max_capacity: process(start, end, box)
    # 현재 박스 개수가 수용 가능한 박스 개수 이상인 경우
    else: process(start, end, max_capacity)

print(total)