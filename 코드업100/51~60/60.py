# 60
a, b = map(int, input().split())
print(bin(a))
print(bin(b))
print(int(bin(a & b), 2))