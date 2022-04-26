import sys
from collections import deque

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())

# 1층 ~ F층, 스타트링크 G층, 현재 S층
# 중복 방문 방지
visited = [False] * (F + 1)

answer = []


def bfs():
    global answer
    q = deque()
    q.append([S, 0, U])
    q.append([S, 0, -D])
    visited[S] = True

    while q:
        now, cnt, move, = q.popleft()
        if now == G:
            answer.append(cnt)

        target = now + move
        if 1 <= target <= F and not visited[target]:
            visited[target] = True
            q.append([target, cnt + 1, U])
            q.append([target, cnt + 1, -D])


bfs()
if len(answer) == 0:
    print("use the stairs")
else:
    print(min(answer))
