import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

length = 0
count = 0
for i in range(len(a)):
    if a[i] > k:
        length = i - 1
        break

for j in range(length, -1, -1):
    #print(f"{k} - {k // a[j]} * {a[j]} = ", end=" ")
    count += k // a[j]
    k -= a[j] * (k // a[j])
    #print(k)

print(count)
