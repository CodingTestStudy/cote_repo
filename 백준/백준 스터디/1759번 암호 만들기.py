from itertools import combinations
L, C = map(int, input().split())
alpha_list = list(input().split())
vowel_list = ['a', 'e', 'i', 'o', 'u']
answer = []
answer_set = set(combinations(alpha_list, L))
for temp in answer_set:
    vowel = 0 # 모음
    consonant = 0 # 자음
    for i in range(len(temp)):
        if temp[i] in vowel_list:
            vowel += 1
        else:
            consonant += 1
    if vowel >= 1 and consonant >= 2:
        answer.append(''.join(sorted(temp)))
answer.sort()
for value in answer:
    print(value)


