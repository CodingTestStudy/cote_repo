def solution(x):
    y = x
    sum_digit = 0
    while x != 0:
        sum_digit += x % 10
        x //= 10
    if y % sum_digit == 0:
        return True
    return False

print(solution(11))

# return n % sum([int(c) for c in str(n)]) == 0
