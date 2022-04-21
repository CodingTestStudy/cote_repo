import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
board = [input() for _ in range(5)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[False] * 5 for _ in range(5)]
answer = 0
answer_list = set()


def dfs(temp, s, y):
    global answer, visited
    # 임도연파가 우위를 점한 경우
    if y >= 4:
        return
    # 이다솜파가 우위를 점한 경우
    if len(temp) == 7 and s >= 4:
        temp = tuple(sorted(temp))
        if temp not in answer_list:
            answer += 1
            answer_list.add(temp)
        return
    for r, c in temp:
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 범위 이탈
            if nr < 0 or nc < 0 or nr >= 5 or nc >= 5:
                continue
            # 방문 여부
            if visited[nr][nc]:
                continue
            temp.append((nr, nc))
            visited[nr][nc] = True
            if board[nr][nc] == 'S':
                dfs(temp, s + 1, y)
            else:
                dfs(temp, s, y + 1)
            temp.pop()
            visited[nr][nc] = False


for r in range(5):
    for c in range(5):
        if board[r][c] == 'S':
            temp = [(r, c)]
            visited[r][c] = True
            dfs(temp, 1, 0)
            visited[r][c] = False
print(answer)
