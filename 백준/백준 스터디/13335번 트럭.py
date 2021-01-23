import sys
from collections import deque

N, W, L = map(int, input().split())
data = deque(map(int, sys.stdin.readline().split()))

visited = [0] * N   # 해당 index 트럭의 다리 방문횟수
time = 0
idx = 0 # 다리에 존재하는 트럭들 중, 가장 앞의 트럭 index
bridge = deque()    # 다리에 존재하는 트럭 리스트
bridge.append(data.popleft())   # 첫번째 index 트럭 다리 방문 시작
while bridge:   # 다리에 트럭이 없을 때까지 반복(즉, 다 지나갔을 때까지)
    time += 1
    for i in range(idx, idx + len(bridge)): # 다리에 존재하는 트럭들을 대상으로
        visited[i] += 1 # 방문처리 누적
        if visited[i] >= W: # W번 방문했다면
            bridge.popleft()  # 맨앞의 트럭 다리에서 탈출
            idx = i + 1 # 그 다음 맨앞에 있는 트럭 index로 갱신
    if len(data) > 0 and sum(bridge) + data[0] <= L:
        # 트럭이 남아있고, 현재 다리위의 트럭 무게와 앞으로 다리에 들어올 트럭의 무게가 다리무게 제한이하라면
        # 트럭 다리에 추가
        bridge.append(data.popleft())
print(time + 1)
