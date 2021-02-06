# 이코테 교재, 기출문제(그리디)
# 만들 수 없는 금액
N = int(input())
weight = list(map(int, input().split()))
weight.sort() # 1 1 2 3 6 7 30

# 초기값 1로 세팅.
# 맨 처음 가장 작은 값과 비교할 때, 1보다 작으면 안되기 때문에
target = 1
for x in weight:
    if target < x: break
    target += x # 측정 가능 값을 누적

# 초기에 target 이 0부터가 아닌 1부터 시작하였기 때문에
# break 문에서 바로 빠져나온 target 값 자체가 측정가능한 최댓값에 1이 더해진 값
# == 측정 불가능한 최솟값
print(target)




