n = int(input())
answer = []


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def dfs(depth, num):
    global answer
    if depth == n - 1:
        if is_prime(int(num)):
            answer.append(num)
        return

    if is_prime(int(num)):
        for i in range(10):
            dfs(depth + 1, num + str(i))


for i in range(2, 10):
    dfs(0, str(i))

answer.sort()
for ans in answer:
    print(ans)
