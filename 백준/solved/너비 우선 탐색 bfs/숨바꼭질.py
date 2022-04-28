import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())  # 수빈, 동생
visited = [-1] * 100001


def check_range(now):
    if 0 <= now <= 100000:
        return True
    return False


# -1, 1, *2
def bfs():
    q = deque()
    q.append(N)
    visited[N] = 0
    while q:
        target = q.popleft()
        if target == K:
            print(visited[target])
            return
        if check_range(target - 1) and visited[target - 1] == -1:
            q.append(target - 1)
            visited[target - 1] = visited[target] + 1
        if check_range(target + 1) and visited[target + 1] == -1:
            q.append(target + 1)
            visited[target + 1] = visited[target] + 1
        if check_range(target * 2) and visited[target * 2] == -1:
            q.append(target * 2)
            visited[target * 2] = visited[target] + 1


bfs()
