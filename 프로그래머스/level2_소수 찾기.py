from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num = [i for i in numbers]
    num_list = []
    for i in range(1, len(num) + 1):
        num_list.append(list(permutations(num, i)))

    answer_list = set()
    for i in range(len(num_list)):
        for j in range(len(num_list[i])):
            str_num = ""
            for k in range(len(num_list[i][j])):
                str_num += num_list[i][j][k]
            answer_list.add(int(str_num))

    for value in answer_list:
        if is_prime(value):
            answer += 1

    return answer

print(solution("17"))
print(solution("011"))