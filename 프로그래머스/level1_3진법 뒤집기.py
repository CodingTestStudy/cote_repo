def solution(n):
    r = 0
    answer_list = []
    while n != 0:
        r = n % 3
        n //= 3
        answer_list.append(r)
    count = 1
    answer = 0
    while answer_list:
        answer += answer_list.pop() * count
        count *= 3

    return answer
print(solution(125))