def solution(word):
    word_dict = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = len(word)
    cnt = (((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1
    for i in word:
        answer += cnt * word_dict[i]
        cnt = (cnt - 1) // 5
    return answer


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))

# # 순열 조합 함수 사용
# from itertools import product
#
#
# def solution(word):
#     word_list = []
#     for i in range(1, 6):
#         word_list += list(map("".join, product("AEIOU", repeat=i)))
#     word_list.sort()
#     return word_list.index(word) + 1

# # 완전 탐색
# def make_word_list(cnt, word, word_list, vowel_list):
#     if cnt == 5:
#         return
#     for i in range(len(vowel_list)):
#         word_list.append(word + vowel_list[i])
#         make_word_list(cnt + 1, word + vowel_list[i], word_list, vowel_list)
#
#
# def solution(word):
#     answer = 0
#     word_list = []
#     vowel_list = ['A', 'E', 'I', 'O', 'U']
#     make_word_list(0, "", word_list, vowel_list)
#     return word_list.index(word) + 1
