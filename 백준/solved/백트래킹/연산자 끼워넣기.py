# 순열 사용 (pypy3 성공, python3 시간초과)
import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
data = list(map(int, input().split()))
calc_data = ["+", "-", "*", "//"]
calc_list = []


def calc_minus(num, q):
    num *= -1
    num //= q
    return num * (-1)


def calculate(x, y, sign):
    if sign == "+":
        return x + y
    elif sign == "-":
        return x - y
    elif sign == "*":
        return x * y
    else:
        if x < 0:
            return calc_minus(x, y)
        else:
            return x // y


for i in range(4):
    for _ in range(data[i]):
        calc_list.append(calc_data[i])
permutation = list(permutations(calc_list, n - 1))

min_value = 1e9
max_value = -1

while permutation:
    per = permutation.pop()
    result = a[0]
    for i in range(n - 1):
        sign = per[i]
        num = a[i + 1]
        result = calculate(result, num, sign)
    min_value = min(min_value, result)
    max_value = max(max_value, result)
print(max_value)
print(min_value)
