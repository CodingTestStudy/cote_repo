def dfs(n, computers, i, visited):
    visited[i] = True
    for j in range(n):
        if i != j and computers[i][j] == 1:
            if not visited[j]:
                dfs(n, computers, j, visited)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            answer += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))