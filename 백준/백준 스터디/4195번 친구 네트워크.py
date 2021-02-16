import sys
T = int(sys.stdin.readline().strip())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[b] = a
        number[a] += number[b]
    print(number[a])


for _ in range(T):
    F = int(sys.stdin.readline().strip())
    friend = dict()
    number = dict()
    for _ in range(F):
        a, b = sys.stdin.readline().strip().split()
        if a not in friend:
            friend[a] = a
            number[a] = 1
        if b not in friend:
            friend[b] = b
            number[b] = 1
        union_parent(friend, a, b)