# 다른 풀이 참고한 코드

def solution(numbers):
    answer = []
    for num in numbers:
        # 임의로 앞에 '0'추가(111 인 경우도 고려)
        bin_num = list('0' + bin(num)[2:])
        # 가장 작은 자리수에 해당하는 0의 위치 찾기
        idx = ''.join(bin_num).rfind('0')
        # 해당 값을 1로 수정, 가장 작은 값으로 수정
        bin_num[idx] = '1'

        # 짝수인 경우는 위의 과정에서 1만 더해진 값으로 수정되어 있기 때문에
        # 수정할 필요 X, 이미 최소값

        # 홀수인 경우, 수정된 위치의 이전자리 값을 0으로 수정하여
        # 이전 값보다 더 작은 값으로 수정
        if num % 2 == 1:
            bin_num[idx + 1] = '0'
        answer.append(int(''.join(bin_num), 2))
    return answer

print(solution([2, 7]))
# 시간초과 코드
# from itertools import combinations
#
# def bin_to_dec(s):
#     result = 0
#     for i in range(len(s)):
#         result += (2 ** (len(s) - i - 1)) * int(s[i])
#     return result
#
#
# def change(s, i):
#     if s[i] == '1':
#         s[i] = '0'
#     else:
#         s[i] = '1'
#     return s
#
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         min_num = 1e9
#         num = "0" + bin(numbers[i])[2:]
#         num_list = [num[x] for x in range(len(num))]
#         items = [i for i in range(len(num_list))]
#         change_index_list1 = list(combinations(items, 1))
#         change_index_list2 = list(combinations(items, 2))
#
#         while change_index_list1:
#             x = change_index_list1.pop()
#             temp_num_list = [num[x] for x in range(len(num))]
#
#             temp = bin_to_dec(change(temp_num_list, x[0]))
#             if numbers[i] < temp < min_num:
#                 min_num = temp
#
#         while change_index_list2:
#             x, y = change_index_list2.pop()
#             temp_num_list = [num[x] for x in range(len(num))]
#             temp = change(temp_num_list, x)
#             temp = bin_to_dec(change(temp, y))
#
#             if numbers[i] < temp < min_num:
#                 min_num = temp
#         answer.append(min_num)
#     return answer