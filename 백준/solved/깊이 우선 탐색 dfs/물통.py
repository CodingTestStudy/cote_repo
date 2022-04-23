import sys
from collections import deque

input = sys.stdin.readline
a, b, c = map(int, input().split())
q = deque()


def move(aa, bb):
    global q
    if not visited[aa][bb]:
        visited[aa][bb] = True
        q.append((aa, bb))


def bfs():
    global q
    # 첫 물통 상태 a, b
    q.append((0, 0))
    visited[0][0] = True
    while q:
        aa, bb = q.popleft()
        # 현재 c의 상태 -> 원래 c 에서 a,b 상태 빼기
        cc = c - aa - bb
        # a 물통이 빈 경우
        if aa == 0:
            answer.append(cc)

        # a -> b, a가 비지 않고 b가 넘치지 않은 경우
        if aa > 0 and bb < b:
            water = min(aa, b - bb)
            move(aa - water, bb + water)
        # a -> c
        if aa > 0 and cc < c:
            water = min(aa, c - cc)
            move(aa - water, bb)
        # b -> a
        if bb > 0 and aa < a:
            water = min(bb, a - aa)
            move(aa + water, bb - water)
        # b -> c
        if bb > 0 and cc < c:
            water = min(bb, c - cc)
            move(aa, bb - water)
        # c -> a
        if cc > 0 and aa < a:
            water = min(a - aa, cc)
            move(aa + water, bb)
        # c -> b
        if cc > 0 and bb < b:
            water = min(b - bb, cc)
            move(aa, bb + water)


# 경우의 수 중복 차단
visited = [[False] * (b + 1) for _ in range(a + 1)]
answer = []
bfs()
answer.sort()
for ans in answer:
    print(ans, end=' ')
