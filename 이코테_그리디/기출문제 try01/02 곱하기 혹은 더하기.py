# 곱하기 혹은 더하기
# 입력 : 여러개의 숫자로 구성된 하나의 문자열 s
# 출력 : 최댓값
# 02984 -> 576
# 567 -> 210

s = input()
result = int(s[0])

for i in range(1, len(s)):
  if result == 0: result += int(s[i])    
  else: result *= int(s[i])
  
print(result)