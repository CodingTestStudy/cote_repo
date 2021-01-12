# 문자열 뒤집기
# 문자열 s (1 <= s의 길이 <= 1,000,000)
s = input()
n = []
for i in s:
  n.append(int(i))

group0 = 0
group1 = 0
for i in range(len(n) - 1):
  if n[i] == 0 and (n[i + 1] == 1 or i + 1 == len(n) - 1):
    group0 += 1
  elif n[i] == 1 and (n[i + 1] == 0 or i + 1 == len(n) - 1):
    group1 += 1

print(min(group0, group1))
 