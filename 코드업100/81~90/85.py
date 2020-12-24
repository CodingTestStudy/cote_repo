# 85
h, b, c, s = map(float, input().split())
result = h * b * c * s / 8 / (pow(1024, 2))
print(round(result, 1), " MB")

# x bit
# x / 8bit -> byte
# x / 8bit / 1024byte -> KB
# x / 8bit / 1024 ^ 2 byte -> MB
# x / 8bit / 1024 ^ 3 byte -> GM