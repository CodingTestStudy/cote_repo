import sys

def dfs(r, c):
    if c == C - 1: # 파이프라인이 끝까지 도달했다면
        return True

    # 오른쪽으로 이동할 수 있는 좌표들 계산
    for d in move:
        nr, nc = r + d[0], c + d[1]

        # 범위 벗어나면, 무시하고 다음 좌표 계산
        if not(0 <= nr < R) or not(0 <= nc < C):
            continue

        # 해당 좌표가 방문한적 없는 좌표라면
        if not visited[nr][nc]:
            visited[nr][nc] = True # 방문 처리

            # 해당 좌표가 파이프라인 끝까지 도달해서 True 를 return 했으면
            if dfs(nr, nc):
                return True
    # 파이프라인 끝까지 도달하지 못했으면
    return False

R, C = map(int, input().split())
pipe = []
visited = [[False] * C for _ in range(R)]
for i in range(R):
    input_data = list(sys.stdin.readline().strip())
    pipe.append(input_data)
    for j in range(C):
        if input_data[j] == 'x':
            visited[i][j] = True

move = [(-1, 1), (0, 1), (1, 1)]
result = 0
for i in range(R):
    if dfs(i, 0): # i번째 행에서 출발했을 때, 파이프라인 끝까지 도달했으면
        result += 1 # 파이라인 개수 증가
print(result)
