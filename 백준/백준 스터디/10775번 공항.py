import sys
G = int(sys.stdin.readline().strip())
P = int(sys.stdin.readline().strip())
plane = []
for _ in range(P):
    plane.append(int(sys.stdin.readline().strip()))


def find_parent(x):
    if x == parent[x]:
        return x
    temp = find_parent(parent[x])
    parent[x] = temp
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    parent[x] = y


parent = {i: i for i in range(G + 1)}
count = 0
for i in plane:
    x = find_parent(i)
    if x == 0:
        break
    union_parent(x, x - 1)
    count += 1
print(count)