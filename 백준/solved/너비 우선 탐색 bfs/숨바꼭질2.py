import sys
from collections import deque, Counter

input = sys.stdin.readline
N, K = map(int, input().split())

visited = [1e9] * 1000001


def check_range(now):
    if 0 <= now <= 100000:
        return True
    return False


def bfs():
    q = deque()
    q.append(N)
    visited[N] = 0
    cnt = 0
    while q:
        target = q.popleft()
        if target == K:
            cnt += 1
            continue
        if check_range(target * 2) and (visited[target * 2] == 1e9 or visited[target * 2] == visited[target] + 1):
            q.append(target * 2)
            visited[target * 2] = visited[target] + 1

        if check_range(target - 1) and (visited[target - 1] == 1e9 or visited[target - 1] == visited[target] + 1):
            q.append(target - 1)
            visited[target - 1] = visited[target] + 1

        if check_range(target + 1) and (visited[target + 1] == 1e9 or visited[target + 1] == visited[target] + 1):
            q.append(target + 1)
            visited[target + 1] = visited[target] + 1

    print(visited[K])
    print(cnt)


bfs()
