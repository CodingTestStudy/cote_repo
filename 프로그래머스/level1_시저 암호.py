def solution(s, n):
    answer = ''
    for value in s:
        if value == ' ':
            answer += ' '
            continue
        change = ord(value) + n
        if 97 <= ord(value) <= 122:
            if change > 122:
                answer += chr(change - 26)
            else:
                answer += chr(change)
        else:
            if change > 90:
                answer += chr(change - 26)
            else:
                answer += chr(change)

    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))

# for i in range(len(s)):
#         if s[i].isupper():
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
#         elif s[i].islower():
#             s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
#
#     return "".join(s)

