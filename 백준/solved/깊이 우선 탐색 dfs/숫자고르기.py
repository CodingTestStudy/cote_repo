import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i].append(int(input()))


def dfs(target):
    # 방문 여부 확인
    if not visited[target]:
        # 방문 처리
        visited[target] = True
        for tar in graph[target]:
            top_set.add(target)
            bottom_set.add(tar)
            # 교집합 확인
            if top_set == bottom_set:
                answer.extend(list(bottom_set))
                return
            dfs(tar)
    # 다음 순환을 위해 방문 처리 취소
    visited[target] = False


answer = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    top_set, bottom_set = set(), set()
    dfs(i)

answer = sorted(list(set(answer)))
print(len(answer))
for ans in answer:
    print(ans)
