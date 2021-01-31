import sys
N = int(sys.stdin.readline().rstrip())
child = list(map(int, sys.stdin.readline().rstrip().split()))
line_position = [0] * (N + 1)

for i in range(1, N + 1):
    n = child[i - 1]
    line_position[n] = line_position[n - 1] + 1

line_position.sort()
print(N - line_position[N])
