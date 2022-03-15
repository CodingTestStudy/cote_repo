# BFS 사용
from collections import deque


def bfs(start, n, graph):
    q = deque()
    q.append(start)
    visited = [False] * (n + 1)
    visited[start] = True
    cnt = 0
    while q:
        now = q.popleft()
        for wire in graph[now]:
            if not visited[wire]:
                cnt += 1
                visited[wire] = True
                q.append(wire)
    return cnt


def solution(n, wires):
    answer = 100
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    for wire in wires:
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])

        first = bfs(wire[0], n, graph)
        second = bfs(wire[1], n, graph)
        answer = min(answer, abs(first - second))

        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))

# # find, union 사용
# from collections import defaultdict
#
#
# def find_parent(parent, x):
#     if x != parent[x]:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent, x, y):
#     x = find_parent(parent, x)
#     y = find_parent(parent, y)
#     if x < y:
#         parent[y] = x
#     else:
#         parent[x] = y
#
#
# def solution(n, wires):
#     answer = 100
#     for i in range(len(wires)):
#         parent = [k for k in range(0, n + 1)]
#
#         for j in range(len(wires)):
#             if i != j:
#                 x, y = wires[j]
#                 if find_parent(parent, x) != find_parent(parent, y):
#                     union_parent(parent, x, y)
#
#         value_dict = defaultdict(int)
#         for index in range(1, n + 1):
#             value_dict[find_parent(parent, index)] += 1
#         value_list = list(value_dict.values())
#         first, second = value_list[0], value_list[1]
#         answer = min(answer, abs(first - second))
#     return answer
