# 곱하기 혹은 더하기
# 문자열 s (1 <= s의 길이 <= 20)
s = input()
n = []
result = 0
for i in s:
  n.append(int(i))

if n[0] == 0 or n[0] == 1:
  result += n[0] + n[1]
else:
  result += n[0] * n[1]

for i in range(2, len(s)):
  if n[i] == 0 or n[i] == 1:
    result += n[i]
  else:
    result *= n[i]
      
print(result)