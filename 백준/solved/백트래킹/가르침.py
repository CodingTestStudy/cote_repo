import sys

input = sys.stdin.readline
n, k = map(int, input().split())
if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

answer = 0
alpha_list = []
for _ in range(n):
    alpha_list.append(input().strip())
learn = [False] * 26

for a in ('a', 'n', 't', 'i', 'c'):
    learn[ord(a) - ord('a')] = True


def dfs(idx, cnt):
    global answer

    if cnt == k - 5:
        result = 0
        for alpha in alpha_list:
            flag = True
            for a in alpha[4:-4]:
                if not learn[ord(a) - ord('a')]:
                    flag = False
                    break
            if flag:
                result += 1
        answer = max(answer, result)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


dfs(0, 0)
print(answer)
