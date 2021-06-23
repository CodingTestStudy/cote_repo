from collections import Counter

def solution(n):
    one = Counter(bin(n))['1']
    for i in range(n + 1,  1000001):
        if Counter(bin(i)[2:])['1'] == one:
            return i


print(solution(78))
print(solution(15))
print(solution(6))