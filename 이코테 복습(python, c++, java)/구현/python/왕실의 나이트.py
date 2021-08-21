s = input()
r = int(s[1])
c = int(ord(s[0])) - int(ord('a')) + 1

d = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

cnt = 0
for i in range(8):
    nr = d[i][0]
    nc = d[i][1]
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        cnt += 1
print(cnt)
