# 두 배열의 원소 교체
# n : 원소 개수 1 <= n <= 100,000
# k : 바꿔치기 연산 최대 횟수 0 <= k <= n
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))
