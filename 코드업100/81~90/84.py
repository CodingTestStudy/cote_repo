# 84
red, green, blue = map(int, input().split())
for i in range(0, red):
  for j in range(0, green):
    for z in range(0, blue):
      print(i, j, z)


print(red * green * blue)