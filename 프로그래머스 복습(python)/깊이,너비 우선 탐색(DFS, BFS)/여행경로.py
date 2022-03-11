from collections import defaultdict


def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        start, end = ticket[0], ticket[1]
        routes[start].append(end)

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = ['ICN']
    while stack:
        target = stack[-1]

        if not routes[target]:
            answer.append(stack.pop())
        else:
            stack.append(routes[target].pop())
    answer.reverse()
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
