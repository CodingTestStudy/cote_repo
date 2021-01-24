import sys
# 파이썬 재귀 횟수가 1000번으로 제한되어 있기 때문에
# 재귀 가능 횟수 임의로 설정
# 설정 안하고 백준 채점시, 에러 발생
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(data, r, c, n, m):
    if not (0 <= r < n) or not (0 <= c < m): # 배추밭의 범위를 벗어나면 False
        return False
    if data[r][c] == 1: # 해당 좌표에 배추가 존재한다면
        data[r][c] = 0  # 해당 좌표방문 처리(?), 앞으로의 재귀에서 추가로 방문하지 않기 위해
        for i in range(4):  # 상하좌우
            # 배추가 존재하는 좌표를 기준으로, 상하좌우 좌표 확인
            dfs(data, r + dx[i], c + dy[i], n, m)
        # 배추가 존재하는 좌표들을 기준으로 상하좌우를 반복적으로 이동한 후
        # 주변이 모두 0인 경우, 배추 모여있는 곳을 모두 확인하면
        # True return -> 배추흰지렁이 1추가
        return True
    return False


t = int(input())  # 테스트 케이스 개수
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []
for _ in range(t):  # 각 테스트 케이스에 대해서
    m, n, k = map(int, input().split()) # 배추 가로, 세로 길이, 배추 개수
    data = [[0] * m for _ in range(n)]  # 배추밭 0으로 초기화

    for _ in range(k):  # 배추의 개수만큼
        column, row = map(int, input().split()) # 배추 존재 위치 입력
        data[row][column] = 1 # 해당 위치 값을 1로 변경(배추 존재)

    count = 0
    # 배추 밭 좌표를 모두 반복문으로 돌면서
    for r in range(n):
        for c in range(m):
            if dfs(data, r, c, n, m):   # 모든 좌표를 dfs함수에서 확인
                # dfs 함수에서 true가 나올 때마다 배추흰지렁이 추가
                # dfs에서 true가 나오는 경우는 배추 무리를 확인한 경우
                count += 1

    result.append(count) # 각 테스트 케이스에서의 배추흰지렁이 수를 저장하는 리스트

for value in result: # 각 테스트 케이스에서
    print(value)    # 배추흰지렁이 수 출력
