import heapq

def dijkstra(start, n, load):
    dist = [int(1e9)] * (n + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        value, destination = heapq.heappop(q)
        if dist[destination] < value:
            continue

        for v, d in load[destination]:
            cost = value + v
            if dist[d] > cost:
                dist[d] = cost
                heapq.heappush(q, (cost, d))
    return dist

def solution(n, s, a, b, fares):
    answer = 0
    load = [[] for _ in range(n + 1)]
    for value in fares:
        s1, s2, dist = value
        load[s1].append((dist, s2))
        load[s2].append((dist, s1))

    dp = [[]] + [dijkstra(i, n, load) for i in range(1, n + 1)]
    answer = int(1e9)
    for i in range(1, n + 1):
        answer = min(answer, dp[s][i] + dp[i][a] + dp[i][b])

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
# print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
# print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
