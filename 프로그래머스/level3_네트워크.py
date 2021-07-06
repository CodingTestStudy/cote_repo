# bfs 사용
from collections import deque
def bfs(n, computers, i, visited):
    # 방문 처리
    visited[i] = True
    q = deque()
    q.append(i)
    while q:
        now = q.popleft()
        # 방문 처리
        visited[now] = True
        for j in range(n):
            # now 번째 컴퓨터, j번째 컴퓨터 서로 다르고, 연결되어 있다면
            if now != j and computers[now][j] == 1:
                # 이전에 방문한적 없는 네트워크라면
                if not visited[j]:
                    # 앞으로 학인할 네트워크 목록에 추가
                    q.append(j)


def solution(n, computers):
    answer = 0
    # 방문 여부 확인(n개의 모든 네트워크 확인할 예정)
    # 이전에 방문했던 네트워크라면 재확인할 필요 없기 때문
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs(n, computers, i, visited)
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# dfs 사용
# def dfs(n, computers, i, visited):
#     # 방문 처리
#     visited[i] = True
#     for j in range(n):
#         # i번째 컴퓨터, j번째 컴퓨터 서로 다르고, 연결되어 있다면
#         if i != j and computers[i][j] == 1:
#             # 이전에 방문한 적 없는 네트워크라면
#             if not visited[j]:
#                 # 해당 네트워크와 연결되어 있는 타 네트워크 확인하기 위해
#                 # 재귀
#                 dfs(n, computers, j, visited)
#
#
# def solution(n, computers):
#     answer = 0
#     # 방문 여부 확인(n개의 모든 네트워크 확인할 예정)
#     # 이전에 방문했던 네트워크라면 재확인할 필요 없기 때문
#     visited = [False for i in range(n)]
#     for i in range(n):
#         if not visited[i]:
#             dfs(n, computers, i, visited)
#             answer += 1
#     return answer