from collections import deque
def solution(cacheSize, cities):

    # 캐시가 존재하지 않을 경우
    if cacheSize == 0:
        return len(cities) * 5

    cache = deque()
    time = 0
    for i in range(len(cities)):
        now = cities[i].lower()
        # 해당 도시가 이미 캐시에 존재할 경우
        if now in cache:
            cache.remove(now)
            cache.append(now)
            time += 1

        # 캐시에 공간이 남아있을 경우(cache hit)
        elif len(cache) < cacheSize:
            cache.append(now)
            time += 5
        # 캐시에 공간이 없을 경우(cache miss)
        else:
            # 가장 맨앞의(가장 오래된) 도시를 제거 후, 새로운 도시 삽입
            cache.popleft()
            cache.append(now)
            time += 5
    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))