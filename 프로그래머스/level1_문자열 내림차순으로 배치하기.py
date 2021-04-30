def solution(s):
    answer = ''
    s_list = list(s)
    s_list.sort(reverse=True)
    for value in s_list:
        answer += value
    #
    # for i in range(len(s_list)):
    #     if 65 <= ord(s_list[i]) <= 90:
    #         s_list.append(s_list[i])
    #     else:
    #         for j in range(i, len(s_list)):
    #             answer += s_list[j]
    #         break

    return answer

print(solution("Zbcdefg"))