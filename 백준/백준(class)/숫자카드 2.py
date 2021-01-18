from bisect import bisect_left, bisect_right
n = int(input())
result = []
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))
for value in m_list:
    x = bisect_right(n_list, value) - bisect_left(n_list, value)
    result.append(x)

for value in result:
    print(value, end=' ')