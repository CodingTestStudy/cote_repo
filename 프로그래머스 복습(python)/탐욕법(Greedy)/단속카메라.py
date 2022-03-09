from collections import deque


def solution(routes):
    answer = 0
    routes = deque(sorted(routes, key=lambda x: x[1]))
    while routes:
        now = routes.popleft()[1]
        while routes:
            start, end = routes[0]
            if start <= now <= end or now >= end:
                routes.popleft()
            else:
                break
        answer += 1
    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
