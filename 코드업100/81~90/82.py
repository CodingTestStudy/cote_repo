# 82
a = int(input(), 16)
b = hex(a)[2].upper() # B

for i in range(1, 16):
  result = hex(a * i)[2:].upper()
  c = hex(i)[2:].upper()
  print(b + "*" + c + "=" + result)
