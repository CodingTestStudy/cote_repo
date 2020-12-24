# 86
width, height, bit = map(int, input().split())
byte = width * height * bit / 8
kb = byte / 1024
mb = kb / 1024
print(round(mb, 2), " MB")
# print(round(byte/pow(1024, 2), 2), " MB")