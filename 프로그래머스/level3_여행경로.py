# 풀이 참고 코드
from collections import defaultdict

def dfs(routes, n):
    stack = ["ICN"]
    path = []
    while stack:
        start = stack[-1]
        # 이미 갔다와서 도착지 목록이 없다면, 해당 경로에 삽입
        if len(routes[start]) == 0:
            path.append(stack.pop())
        # 그렇지 않다면,
        else:
            # 스택에 쌓음과 동시에 기존 tickets 에서 해당 도착지점 정보 삭제
            stack.append(routes[start].pop(0))

    return path[::-1]

def solution(tickets):
    routes = defaultdict(list)
    for key, value in tickets:
        routes[key].append(value)

    # 출발지가 같지만, 여러 도착지점이 존재하는 경우,
    # 사전순으로 진행되기 때문에 정렬 수행
    for r in routes:
        routes[r].sort()

    answer = dfs(routes, len(routes))
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# 시간 초과
# def solution(tickets):
#     answer = []
#     tickets.sort()
#     start = ""
#     end = ""
#     for i in range(len(tickets)):
#         if tickets[i][0] == "ICN":
#             start = tickets[i][0]
#             end = tickets[i][1]
#             answer.append(start)
#             answer.append(end)
#             del tickets[i]
#             break
#     while tickets:
#         for i in range(len(tickets)):
#             if tickets[i][0] == end:
#                 end = tickets[i][1]
#                 answer.append(end)
#                 del tickets[i]
#                 break
#
#     return answer