n = int(input())
data = map(int, input().split())
result = 0
def is_prime(x):
    count = 0
    if x == 1:
        return False
    for i in range(2, x + 1):
        if x % i == 0: count += 1
    if count == 1: return True
    else: return False

for value in data:
    if is_prime(value):
        result += 1

print(result)