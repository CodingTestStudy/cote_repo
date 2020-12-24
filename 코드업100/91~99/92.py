# 92
from math import gcd

a, b, c = map(int, input().split())
day = 1

while day % a | day % b | day % c != 0: day += 1
print(day)



# 최소 공배수 사용
def lcm(x, y):
  return x * y // gcd(x, y)

print(lcm(lcm(a, b), c))