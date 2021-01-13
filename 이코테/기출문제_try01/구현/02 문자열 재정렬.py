# 문자열 재정렬
# (1 <= s의 길이 <= 10,000)
s = input()
alphabet = []
number = 0

# if value.isalpha():
for value in s:
    if 48 <= ord(value) <= 57:
        number += int(value)
    else:
        alphabet.append(value)

alphabet.sort()

alphabet += str(number)
for i in alphabet:
    print(i, end='')
