# 큰 수의 법칙
# n : 입력받는 데이터 개수, 2 <= n <= 1,000
# m : 총 더하는 횟수, 1 <= m <= 10,000
# k : 연속으로 더할 수 있는 최대 횟수, 1 <= k <= 10,000
# k <= m
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
first = data[0]
second = data[1]
result = (m // (k + 1)) * (first * k + second) + (m % (k + 1)) * first
print(result)

