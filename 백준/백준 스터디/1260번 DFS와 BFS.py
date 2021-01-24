import sys
from collections import deque
sys.setrecursionlimit(10000) # 파이썬에서 제한된 재귀 횟수 임의로 재설정

def dfs(array, v, visited):
    print(v, end=' ') # 해당 정점 출력
    visited[v] = True # 해당 정점 방문 처리
    array[v].sort() # 여러군데 방문 가능한 경우, 정점 번호 작은 것 먼저 방문하기 위해 정렬
    for value in array[v]: # 정점과 연결된 다른 정점들에 대해서
        if not visited[value]: # 이전에 방문한 적 없다면
            dfs(array, value, visited) # dfs 함수, 재귀함수

def bfs(array, v, visited):
    q = deque() # 삽입된 순서대로 확인하기 위해, popleft() 사용하기 위해
    q.append(v) # 해당 정점 별도의 리스트에 삽입
    visited[v] = True # 해당 정점 방문 처리
    while q: # 리스트가 빌 때까지
        data = q.popleft() # 가장 먼저 리스트에 들어온 정점
        print(data, end=' ') # 해당 정점 출력
        for value in array[data]: # 해당 정점에 연결된 다른 정점들에 대해서
            if not visited[value]: # 이전에 방문한 적이 없다면
                q.append(value) # 리스트에 삽입 후
                visited[value] = True # 방문 처리


# N : 정점의 개수, M : 간선의 개수, V : 탐색할 정점의 번호
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited1 = [False] * (N + 1) # 방문 초기화
visited2 = [False] * (N + 1) # 방문 초기화
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    # 간선이 양방향이기 때문에 둘다 append()
    graph[start].append(end)
    graph[end].append(start)

dfs(graph, V, visited1)
print()
bfs(graph, V, visited2)