# 이코테 교재, 기출문제(그리디)
# 만들 수 없는 금액
N = int(input())
weight = list(map(int, input().split()))
weight.sort()
# 1 1 2 3 6 7 30
target = 1
for x in weight:
    if target < x: break
    target += x
print(target)




