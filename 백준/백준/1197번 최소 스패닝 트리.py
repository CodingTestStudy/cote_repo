# 크루스칼 알고리즘 사용
def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(x, parent)
    y = find_parent(y, parent)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
tree = []
for _ in range(e):
    tree.append(list(map(int, input().split())))
tree.sort(key=lambda x: x[2])

answer = 0
for start, end, dist in tree:
    if find_parent(start, parent) != find_parent(end, parent):
        union_parent(parent, start, end)
        answer += dist
print(answer)
