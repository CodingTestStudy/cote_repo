n = int(input())
m = []
for _ in range(n):
    m.append(int(input()))
m.sort(reverse=True)
for i in m:
    print(i, end=' ')