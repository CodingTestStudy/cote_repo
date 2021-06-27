def solution(s):
    zero_count = 0
    change = 0
    while s != '1':
        one_count = 0
        for i in range(len(s)):
            if s[i] == '1':
                one_count += 1

        zero_count += (len(s) - one_count)
        s = str(bin(one_count)[2:])
        change += 1

    return [change, zero_count]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))

# more simple code
# def solution(s):
#     change, zero = 0, 0
#     while s != '1':
#         change += 1
#         num = s.count('1')
#         zero += len(s) - num
#         s = bin(num)[2:]
#     return [change, zero]
