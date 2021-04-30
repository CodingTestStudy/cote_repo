def solution(s):
    answer = ''
    s_split = s.split(' ')
    for i in range(len(s_split)):
        s_list = list(s_split[i])
        for j in range(len(s_list)):
            if j % 2 == 0:
                s_list[j] = s_list[j].upper()
            else:
                s_list[j] = s_list[j].lower()
        s_split[i] = "".join(s_list)
    answer = " ".join(s_split)

    return answer

print(solution("try hello world"))


# def solution(s):
#     answer = ''
#     for word in s.split(" "):
#         n = ''
#         for i in range(len(word)):
#             if i%2 == 0 :
#                 n += word[i].upper()
#             else :
#                 n += word[i].lower()
#         answer += (n + " ")
#     return answer[0:-1]