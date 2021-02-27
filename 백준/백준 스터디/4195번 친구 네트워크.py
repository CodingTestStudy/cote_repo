import sys
T = int(sys.stdin.readline().strip())

# 부모노드를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 노드를 합치는 함수
def union_parent(parent, a, b):
    # 각 노드의 부모 노드를 찾는다.
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b: # 서로 다른 집합이라면(서로 부모 노드가 다르다면)
        parent[b] = a # 집합을 합쳐준다. (b가 a에 속하게됨)
        number[a] += number[b] # 집단이 합쳐졌기 때문에, b 집단의 구성원 수를 a 집단에 합쳐준다.
    print(number[a]) # 현재 a 집단의 구성원 수 출력


for _ in range(T):
    F = int(sys.stdin.readline().strip())
    friend = dict()
    number = dict()
    for _ in range(F):
        a, b = sys.stdin.readline().strip().split()
        # 입력받은 a, b가 friend 에 존재하는지 확인
        # 존재하지 않으면, 자기자신을 부모 노드를 설정 해주고,
        # 본인만의 집단에 속하기 때문에, 구성원 수를 1로 설정
        if a not in friend:
            friend[a] = a
            number[a] = 1
        if b not in friend:
            friend[b] = b
            number[b] = 1
        union_parent(friend, a, b)