def distance(start, end):
    start = str(start)
    end = str(end)
    location = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
        '*': (3, 0), '0': (3, 1), '#': (3, 2),
    }

    abs_r = abs(location[start][1] - location[end][1])
    abs_c = abs(location[start][0] - location[end][0])
    return abs_r + abs_c

def solution(numbers, hand):
    answer = ''
    now_l = '*'
    now_r = '#'
    for value in numbers:
        if value in [1, 4, 7]:
            answer += 'L'
            now_l = value
        elif value in [3, 6, 9]:
            answer += 'R'
            now_r = value
        else:
            l_distance = distance(now_l, value)
            r_distance = distance(now_r, value)
            if l_distance < r_distance:
                answer += 'L'
                now_l = value
            elif l_distance > r_distance:
                answer += 'R'
                now_r = value
            else:
                if hand == 'left':
                    answer += 'L'
                    now_l = value
                else:
                    answer += 'R'
                    now_r = value
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))

# def solution(numbers, hand):
#     answer = ''
#     now = [10, 12]
#     for value in numbers:
#         if value % 3 == 1:
#             answer += 'L'
#             now[0] = value
#         elif value % 3 == 0:
#             answer += 'R'
#             now[1] = value
#         else:
#             value = 11 if value == 0 else value
#
#             absL = abs(value - now[0])
#             absR = abs(value - now[1])
#             absL_sum = sum(divmod(absL, 3))
#             absR_sum = sum(divmod(absR, 3))
#
#             if absL_sum > absR_sum:
#                 answer += 'R'
#                 now[0] = value
#             elif absL_sum < absR_sum:
#                 answer += 'L'
#                 now[1] = value
#             else:
#                 if hand == 'left':
#                     answer += 'L'
#                     now[0] = value
#                 else:
#                     answer += 'R'
#                     now[1] = value
#     return answer
