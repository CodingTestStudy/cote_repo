from collections import deque
import sys
K = int(sys.stdin.readline().strip())
W, H = map(int, sys.stdin.readline().strip().split())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(H)]

# 원숭이 상하좌우
mr = [-1, 1, 0, 0]
mc = [0, 0, -1, 1]
# 말 이동 가능 범위(8가지)
hr = [-1, -2, -2, -1, 1, 2, 2, 1]
hc = [-2, -1, 1, 2, -2, -1, 1, 2]

def bfs():
    q = deque()
    q.append((0, 0, K))
    # 같은 좌표에서라도 말 이동방식을 이용해서 도착했는지 안했는지에 따라 값이 다를 수 있기 때문에
    # 각 좌표에 말 이동방식 잔여 횟수를 포함한 3차원 리스트로 값들을 할당한다
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    while q:
        r, c, t = q.popleft()
        # 해당 좌표가 도착지점이라면, 도착지점에 할당된 값 return
        # 해당 좌표에 도착하는 방식이 여러개 있을지라도 가장 먼저 도착한 리스트 값이 최소이다.
        if r == H - 1 and c == W - 1: return visited[r][c][t]
        for i in range(4): # 원숭이 방식
            nr = r + mr[i]
            nc = c + mc[i]
            if not(0 <= nr < H) or not(0 <= nc < W): continue # 범위 벗어남
            if data[nr][nc] == 1: continue # 장애물 존재
            if visited[nr][nc][t]: continue # 방문한적 있음 (말 방식 횟수 t번 남아있는 상태에서의 좌표)
            else:
                visited[nr][nc][t] = visited[r][c][t] + 1 # 이전 좌표값에서 증가
                q.append((nr, nc, t))
        if t > 0: # 말 방식 횟수가 남아 있다면
            for i in range(8): # 말 방식
                nr = r + hr[i]
                nc = c + hc[i]
                if not(0 <= nr < H) or not(0 <= nc < W): continue # 범위 벗어남
                if data[nr][nc] == 1: continue # 장애물 존재
                if visited[nr][nc][t - 1]: continue # 방문한적 있음 (말 방식 1회 사용한 시점)
                else:
                    visited[nr][nc][t - 1] = visited[r][c][t] + 1 # 이전의 좌표값에서 증가 (말 방식 1회 사용 의미로 t - 1)
                    q.append((nr, nc, t - 1)) # 말 방식 1회 사용 의미로 t - 1
    return -1 # q가 빌때까지 도착 지점에 간적이 없다면
print(bfs())