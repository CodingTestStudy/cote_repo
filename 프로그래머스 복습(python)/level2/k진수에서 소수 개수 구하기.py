def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def change(n, k):
    temp = ''
    while n:
        temp += str(n % k)
        n //= k
    return temp[::-1]


def solution(n, k):
    answer = 0
    temp = []
    word = change(n, k).split('0')
    for w in word:
        if len(w) > 0:
            temp.append(w)
    result = list(map(int, temp))
    for value in result:
        if is_prime(value):
            answer += 1
    return answer


print(solution(10, 3))
print(solution(437674, 3))
print(solution(110011, 10))
print(solution(524287, 2))
