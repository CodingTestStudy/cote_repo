import sys
G = int(sys.stdin.readline().strip())
P = int(sys.stdin.readline().strip())
planes = []
parent = [i for i in range(G + 1)] # 자기자신을 부모노드로 초기화
for _ in range(P):
    planes.append(int(sys.stdin.readline().strip()))

# 부모 노드를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 집합을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

count = 0
for plane in planes:
    x = find_parent(parent, plane)
    if x == 0: break # 해당 부모노드가 0이라면, 더이상 도킹할 공간이 없다는 의미
    union_parent(parent, x, x - 1)
    count += 1
print(count)
