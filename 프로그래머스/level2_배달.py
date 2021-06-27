# 못 푼 문제
import heapq

def dijkstra(start, road, distance):
    # start -> start = 0
    distance[start] = 0
    # 도시간의 거리가 최소인 순을 확인하기 위한 큐
    q = []
    heapq.heappush(q, (0, start)) # 거리, 도시

    # 모든 도시<->도시 데이터를 확인할 때까지 반복
    while q:
        dist, now = heapq.heappop(q)
        # 이전의 거리가 더 짧다면 갱신할 필요 X
        if distance[now] < dist:
            continue

        # 도착지 도시가 road 정보에 존재한다면
        # 기존의 거리보다 새로운 거리가 더 짧다면 distance 갱신 후, q에 삽입
        for r in road:
            if r[0] == now:
                cost = dist + r[2]
                next = r[1]
                if cost < distance[next]:
                    distance[next] = cost
                    heapq.heappush(q, (cost, next))
            elif r[1] == now:
                cost = dist + r[2]
                next = r[0]
                if cost < distance[next]:
                    distance[next] = cost
                    heapq.heappush(q, (cost, next))
    return distance

def solution(N, road, K):
    answer = 0
    start = 1
    max_dist = 10000 * N + 1
    distance = [max_dist] * (N + 1)
    dijkstra(start, road, distance)

    for d in distance:
        if d <= K:
            answer += 1
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))