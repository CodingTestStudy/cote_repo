import sys
N = int(sys.stdin.readline().strip())
crane = sorted(list(map(int, sys.stdin.readline().strip().split())), reverse=True)
M = int(sys.stdin.readline().strip())
box = sorted(list(map(int, sys.stdin.readline().strip().split())), reverse=True)

visited = [False for _ in range(M)] # 각 박스에 방문여부 확인
position = [0] * N # 각 크레인의 위치
count = 0
time = 0

# 박스 최대값이 크레인의 최대값보다 크다면
if box[0] > crane[0]: print(-1)
else:
    while count < len(box): # 모든 박스를 확인할 때까지 반복
        for i in range(N): # 모든 크레인에 대해서
            while position[i] < len(box): # 해당 크레인이 모든 박스를 확인하기 전까지
                # 이전에 다룬적이 없는 박스이고, 해당 크레인이 해당 박스보다 크거나 같다면, 옮김 처리
                if not visited[position[i]] and crane[i] >= box[position[i]]:
                    visited[position[i]] = True # 해당 박스 다룸처리
                    position[i] += 1 # i번째 크레인의 위치 이동
                    count += 1 # count번째 박스 처리 완료
                    break
                # 위의 조건에 만족하지 않는다면, 다음 박스를 다루기 위해서 크레인 위치 이동
                position[i] += 1
        # for문을 통해 N개의 크레인의 처리가 모두 이뤄져야 time 증가
        time += 1
    print(time)
