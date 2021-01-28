import sys
n = int(input())
m = int(input())
graph = [[] * (n + 1) for _ in range(m + 1)]
invite = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for value in graph[1]:
    invite.append(value)

for i in range(len(invite)): # 2, 3
    for ff in graph[invite[i]]: # 2, 3의 친구들에 대해서
        if ff not in invite: # 이미 초대목록에 존재하지 않는다면
            invite.append(ff) # 초대 목록에 추가

print(len(invite) - 1) # 자기자신 빼기