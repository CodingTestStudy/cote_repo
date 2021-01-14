n = int(input()) # 1 <= n <= 1,000
p = list(map(int, input().split())) # 1 <= p <= 1,000
p.sort()
result = 0
for i in range(len(p)):
    for j in range(i + 1):
        result += p[j]

print(result)

