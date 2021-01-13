# 뱀
# N : 보드의 크기 (2 <= N <= 100)
# K : 사과의 개수 (0 <= K <= 100)
# 사과의 위치 (K줄)
# L : 뱀의 방향 변환 횟수 (1 <= L <= 100)
# 방향 변환 정보 (X, C)
# X : 몇 초뒤에 C : L(left) or D(right) 방향으로 90도 회전
n = int(input())  # 맵 크기
game_map = [[0] * (n + 2) for _ in range(n + 2)]
map_size = len(game_map)

k = int(input())  # 사과
apple_location = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
  x, y = map(int, input().split())
  game_map[x][y] = 2  # 사과 위치 2로 지정

l = int(input())  # 뱀의 방향 변환 횟수
turn_time_direction = []
for _ in range(l):
  time, direction = input().split()
  turn_time_direction.append((time, direction))

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]



