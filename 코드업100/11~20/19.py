# 19
y, m, d = map(int, (input("y.m.d 입력 : ").split(".")))
print("%04d.%02d.%02d" % (y, m, d))
print(f"{y:02d}.{m:02d}.{d:02d}")