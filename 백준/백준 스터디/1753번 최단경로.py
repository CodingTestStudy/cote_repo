import sys
import heapq

INF = int(1e9)
V, E = map(int, sys.stdin.readline().strip().split())
K = int(sys.stdin.readline().strip())
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, end = heapq.heappop(q)
        # 이전에 다뤘던 거리라면 무시
        if distance[end] < dist: continue

        for i in graph[end]: # end 정점와 연결된 다른 정점들에 대해서
            cost = dist + i[1] # end 정점까지 거리 + end 정점에서 다른 정점까지 거리
            if cost < distance[i[0]]: # end 정점을 거쳐서 간 거리가 더 짧다면
                distance[i[0]] = cost # 더 짧은 거리로 갱신
                heapq.heappush(q, (cost, i[0])) # 해당 거리와 정점 q 리스트에 삽입
dijkstra(K)

for i in range(1, V + 1): # 모든 정점들에 대해서
    if distance[i] == INF: # 해당 정점에 도달하지 못하는 경우
        print("INF")
    else:
        print(distance[i])