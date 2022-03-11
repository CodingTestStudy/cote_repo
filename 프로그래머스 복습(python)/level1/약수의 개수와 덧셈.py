import math


def calculate(target):
    count = 0
    for i in range(1, int(math.sqrt(target)) + 1):
        if target % i == 0:
            if target // i == i:
                count += 1
            else:
                count += 2
    if count % 2 == 0:
        return True
    else:
        return False


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if calculate(i):
            answer += i
        else:
            answer -= i
    return answer


# more simple code
# 제곱수의 약수는 홀수개(같은 숫자끼리 곱하는 경우, 약수의 개수를 총합할 때 1개를 더하기 때문에)
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer

print(solution(13, 17))
print(solution(24, 27))
