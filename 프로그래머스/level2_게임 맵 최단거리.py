from collections import deque

def solution(maps):
    q = deque()
    # 초기 좌표 삽입
    q.append((0, 0))
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 모든 위치를 방문할 때까지 반복
    while q:
        x, y = q.popleft()
        # x, y 좌표의 상하좌우에 대한 정보 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # nx, ny 좌표가 범위에 포함된다면
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                # 해당 좌표가 통로이고 이전에 방문하 적이 없다면
                if maps[nx][ny] == 1:
                    # 이전 좌표보다 한칸 더 전진한 값으로 갱신
                    maps[nx][ny] = maps[x][y] + 1
                    # 해당 좌표를 q에 삽입
                    q.append((nx, ny))

    # 도착지점에 도착할 수 업는 경우
    if maps[len(maps) - 1][len(maps[0]) - 1] == 1:
        return -1
    # 도착지점까지의 전진한 거리 중 최소값 리턴
    return maps[len(maps) - 1][len(maps[0]) - 1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))