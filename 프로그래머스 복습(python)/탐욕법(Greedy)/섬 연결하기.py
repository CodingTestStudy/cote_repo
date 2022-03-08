def find_parent(parent, x):
    if x != parent[x]:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    parent = [i for i in range(n)]

    for d1, d2, cost in costs:
        if find_parent(parent, d1) != find_parent(parent, d2):
            union_parent(parent, d1, d2)
            answer += cost
            n -= 1
        if n == 1:
            break
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))