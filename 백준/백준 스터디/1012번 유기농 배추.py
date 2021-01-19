import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(data, r, c, n, m):
    if not (0 <= r < n) or not (0 <= c < m):
        return False
    if data[r][c] == 1:
        data[r][c] = 0
        for i in range(4):
            dfs(data, r + dx[i], c + dy[i], n, m)
        return True
    return False


t = int(input())  # 테스트 케이스 개수
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []
for _ in range(t):
    m, n, k = map(int, input().split())
    data = [[0] * m for _ in range(n)]

    for _ in range(k):
        column, row = map(int, input().split())
        data[row][column] = 1

    count = 0
    for r in range(n):
        for c in range(m):
            if dfs(data, r, c, n, m):
                count += 1

    result.append(count)

for value in result:
    print(value)
