from itertools import permutations
from math import sqrt


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    num_list = [numbers[i] for i in range(len(numbers))]
    iter_list = []
    for i in range(1, len(num_list) + 1):
        iter_list.append(permutations(num_list, i))
    temp = set()
    for iterator in iter_list:
        for it in iterator:
            temp_num = ''
            for i in range(len(it)):
                temp_num += it[i]
            temp.add(int(temp_num))
    answer = 0
    for value in temp:
        if is_prime(value):
            answer += 1
    return answer


print(solution("17"))
print(solution("011"))