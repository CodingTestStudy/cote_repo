import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
k = int(input())


# 순환하면서 다음 노드에 반대되는 색으로 처리
# 만약 같은 색이 되면 return False

def dfs(v, color):
    visited[v] = color
    for nxt in graph[v]:
        # 첫 방문인 경우
        if visited[nxt] == 0:
            # 다음 노드에 반대되는 색을 처리하고 다음 결과 return
            temp = dfs(nxt, -color)
            # 결과가 같은 color를 만난 경우
            if not temp:
                return False
        # 이전에 방문했는데, 이전의 color와 일치하는 경우
        elif visited[nxt] == visited[v]:
            return False
    return True


for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, v + 1):
        if not visited[i]:
            flag = dfs(i, 1)
            if not flag:
                break

    if flag:
        print("YES")
    else:
        print("NO")
