import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    visited = [False] * (N + 1)
    request = []
    for i in range(1, M + 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        request.append((a, b))
    request.sort(key=lambda x: x[1])

    count = 0
    while request:
        start, end = request.pop(0)
        for i in range(start, end + 1):
            if not visited[i]:
                visited[i] = True
                count += 1
                break
    print(count)
