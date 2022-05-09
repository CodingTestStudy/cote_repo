# ?, ? 의 최대 공약수, 최소 공배수
import math, sys

sys.setrecursionlimit(10 ** 5)

gcd, lcm = map(int, input().split())
answer1, answer2 = 0, 0
diff = 1e9


# 유클리드 호제법
def find_gcd(a, b):
    temp = 0
    while a != 0:
        temp = b % a
        b = a
        a = temp
    return b


def find_pair(target):
    global answer1, answer2, diff
    for i in range(1, int(math.sqrt(target)) + 1):
        if target % i == 0:
            n1, n2 = i, target // i
            if gcd == find_gcd(n1 * gcd, n2 * gcd):
                if diff > n1 + n2:
                    diff = n1 + n2
                    answer1, answer2 = n1 * gcd, n2 * gcd


find_pair(lcm // gcd)
print(answer1, answer2)
