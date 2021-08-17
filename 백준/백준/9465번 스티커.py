T = int(input())
for _ in range(T):
    N = int(input())
    sticker = []
    sticker.append(list(map(int, input().split())))
    sticker.append(list(map(int, input().split())))
    if N == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue
    sticker[0][1] += sticker[1][0]
    sticker[1][1] += sticker[0][0]
    for i in range(2, N):
        sticker[0][i] += max(sticker[1][i - 1], sticker[1][i - 2])
        sticker[1][i] += max(sticker[0][i - 1], sticker[0][i - 2])
    print(max(sticker[0][N - 1], sticker[1][N - 1]))
