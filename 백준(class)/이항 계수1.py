n, k = map(int, input().split())
nk = 1
nn = 1
for i in range(1, k + 1):
    nn *= n + 1 - i
    nk *= i

print(int(nn/nk))
