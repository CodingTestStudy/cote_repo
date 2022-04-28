import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
visited = [-1] * 100001
parent = [0] * 100001


def check_range(now):
    if 0 <= now <= 100000:
        return True
    return False


def print_path(num):
    path = deque()
    while num != -1:
        path.appendleft(num)
        num = parent[num]
    print(*path)


def bfs():
    q = deque()
    q.append(N)
    parent[N] = -1

    visited[N] = 0
    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            print_path(x)
            return

        for num in (x * 2, x - 1, x + 1):
            if check_range(num) and visited[num] == -1:
                q.append(num)
                visited[num] = visited[x] + 1
                parent[num] = x


bfs()
