import sys
N = int(sys.stdin.readline().strip()) # 병정 수
M = int(sys.stdin.readline().strip()) # 접촉 정보 수
virus_list = [[] for _ in range(N + 1)]
x = set()
x.add(1) # 감염자 리스트
for _ in range(M):
    first, second = map(int, sys.stdin.readline().strip().split())
    virus_list[first].append(second)
    virus_list[second].append(first)

for value in virus_list[1]:
    x.add(value)
    for value2 in virus_list[value]:
        x.add(value2)

# print(x)
if len(x) == 1: print(-1)
else: print(len(x) - 1)
