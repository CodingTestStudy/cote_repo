# 64
a, b, c = map(int, input().split())
min1 = a if a < b else b
min2 = min1 if min1 < c else c
print(min2)