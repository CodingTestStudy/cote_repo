s = input()
alpha = []
num = 0
for i in range(len(s)):
    if s[i].isalpha():
        alpha.append(s[i])
    else:
        num += int(s[i])
alpha.sort()
if num != 0:
    alpha.append(str(num))
answer = ''.join(alpha)
print(answer)
