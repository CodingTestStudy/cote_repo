# Prim 알고리즘 사용
import sys
import heapq

input = sys.stdin.readline
v, e = map(int, input().split())
visited = [False] * (v + 1)
tree = [[] for _ in range(v + 1)]

for _ in range(e):
    start, end, dist = map(int, input().split())
    tree[start].append([dist, end])
    tree[end].append([dist, start])

answer = 0
q = []

# 정점 1에서 시작. 거리는 0(1 -> 1)
heapq.heappush(q, [0, 1])
cnt = 0
while q:
    if cnt == v:
        break

    # 현재 그래프에서 가장 짧은 경로 찾기
    d, s = heapq.heappop(q)
    if not visited[s]:
        visited[s] = True
        answer += d
        cnt += 1
        for nxt in tree[s]:
            heapq.heappush(q, nxt)
print(answer)

# # 크루스칼 알고리즘 사용
# def find_parent(x, parent):
#     if x != parent[x]:
#         parent[x] = find_parent(parent[x], parent)
#     return parent[x]
#
#
# def union_parent(parent, x, y):
#     x = find_parent(x, parent)
#     y = find_parent(y, parent)
#
#     if x < y:
#         parent[y] = x
#     else:
#         parent[x] = y
#
#
# v, e = map(int, input().split())
# parent = [i for i in range(v + 1)]
# tree = []
# for _ in range(e):
#     tree.append(list(map(int, input().split())))
# tree.sort(key=lambda x: x[2])
#
# answer = 0
# for start, end, dist in tree:
#     if find_parent(start, parent) != find_parent(end, parent):
#         union_parent(parent, start, end)
#         answer += dist
# print(answer)
