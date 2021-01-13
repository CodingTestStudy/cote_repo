# 02984 -> 576
import time

data = input()
start = time.time()
result = int(data[0])
for i in range(1, len(data)):
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)
print(time.time()-start)


