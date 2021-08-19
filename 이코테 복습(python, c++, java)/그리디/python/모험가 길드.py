n = int(input())
group = list(map(int, input().split()))
group.sort()
group_cnt = 0
total = 0
for i in range(len(group)):
    total += 1
    if total >= group[i]:
        total = 0
        group_cnt += 1

print(group_cnt)
