def solution(s):
    str = s[1:-1]
    s_list = str.split('{')
    result = {}
    for i in range(len(s_list)):
        s_list[i] = s_list[i][:-1]
        if len(s_list[i]) != 0:
            if i != len(s_list) - 1:
                s_list[i] = s_list[i][:-1]
        x = s_list[i].split(',')
        result[len(x)] = x

    answer = []
    for i in range(min(result.keys()), max(result.keys()) + 1):
        for value in result[i]:
            if value not in answer:
                answer.append(value)
    return [int(i) for i in answer]


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

# def solution(s):
#     answer = []
#     s1 = s.lstrip('{').rstrip('}').split('},{')
#
#     new_s = []
#     for i in s1:
#         new_s.append(i.split(','))
#
#     new_s.sort(key = len)
#
#     for i in new_s:
#         for j in range(len(i)):
#             if int(i[j]) not in answer:
#                 answer.append(int(i[j]))
#
#     return answer
#
# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# print(solution("{{20,111},{111}}"))
# print(solution("{{123}}"))
# print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
