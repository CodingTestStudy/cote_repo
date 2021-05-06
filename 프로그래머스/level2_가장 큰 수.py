def solution(numbers):
    numbers = list(map(str, numbers)) # 문자열로 전환 후
    # 최대 자릿수가 3자리수이므로, 최소 3자리수까지 해당 값을 반복하여 붙인다.
    # 문자열을 정렬하면, ASCII 순서로 정렬되기 때문에
    # 앞 문자들 순으로 정려된다. 3자리수까지 반복된 값들을 ASCII 순으로 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)

    # 의미없는 0들을 없애기 위해 int형 변환
    return str(int(''.join(numbers)))

print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2]))


# 시간초과
# from itertools import permutations
# def solution(numbers):
#     num_list = list(permutations(list(map(str, numbers)), len(numbers)))
#     answer = []
#
#     while num_list:
#         answer.append(int("".join(num_list.pop())))
#     return str(max(answer))
#
# print(solution([3, 30, 34, 5, 9]))