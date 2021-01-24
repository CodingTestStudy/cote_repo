import sys
from collections import deque

input = sys.stdin.readline
# 나이트의 위치를 기준으로 이동할 수 있는 위치에 대한 연산
move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]


# 체스판 한 변 길이, 출발 좌표, 도착 좌표
def bfs(length, start_r, start_c, end_r, end_c):
    visited = [[False] * length for _ in range(length)] # 모든 좌표에 방문여부 False 로 초기화
    count = 0 # 이동 횟수 초기화
    q = deque()
    q.append((start_r, start_c)) # 출발 좌표 삽입
    visited[start_r][start_c] = True # 출발 좌표 방문 처리
    while q: # q가 빌 때까지
        q_length = len(q)
        for _ in range(q_length): # q에 삽입되어 있는 데이터 개수만큼
            r, c = q.popleft()
            if r == end_r and c == end_c: # 해당 좌표가 도착 좌표라면
                return count # 이동 횟수 리턴
            for j in range(8): # 나이트가 이동 가능한 8가지 방법에 대해서
                nr = r + move[j][0]
                nc = c + move[j][1]
                # 이동 가능한 좌표들 중에서, 체스판 범위를 벗어나지 않고, 기존에 방문한 적이 없다면
                if 0 <= nr < length and 0 <= nc < length and not visited[nr][nc]:
                    q.append((nr, nc)) # 리스트에 삽입 후
                    visited[nr][nc] = True # 방문 처리
        count += 1 # 위의 과정을 마치고, 나이트 이동 횟수 증가가

N = int(input()) # 테스트 케이스 횟수 입력
L = [] # 각 테스트 케이스에서의 체스판 한 변의 길이를 저장하는 리스트
before = [] # 현재 나이트의 위치를 저장하는 리스트
after = [] # 나이트가 도달하고자 하는 위치를 저장하는 리스트
for _ in range(N):
    L.append(int(input())) # 각 테스트 케이스에서의 체스판 한 변의 길이 입력
    before.append(list(map(int, input().split())))
    after.append(list(map(int, input().split())))

for i in range(N): # 각 테스트 케이스에서의 결과 출력
    print(bfs(L[i], before[i][0], before[i][1], after[i][0], after[i][1]))
