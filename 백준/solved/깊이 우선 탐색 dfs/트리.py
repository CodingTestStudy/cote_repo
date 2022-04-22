import sys

input = sys.stdin.readline
n = int(input())
node = list(map(int, input().split()))
target = int(input())
answer = 0


def dfs(node, tar):
    # 삭제 처리
    node[tar] = -1e9
    for i in range(n):
        if tar == node[i]:
            dfs(node, i)


dfs(node, target)
for i in range(n):
    if node[i] != -1e9 and i not in node:
        answer += 1
print(answer)