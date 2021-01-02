# 문자열 뒤집기
# 입력 : 0 과 1로만 이루어진 문자열 s
# 출력 : 뒤집기 최소 횟수
# 0001100 -> 1
s = input()
count0 = 0 # 0을 뒤집는 횟수
count1 = 0 # 1을 뒤집는 횟수
if s[0] == '0' : count0 += 1
else: count1 += 1

for i in range(len(s) - 1):
  # 각각 숫자가 바뀌는 구간에서만 count횟수 추가
  if s[i] == '0' and s[i+1] == '1': count1 += 1    
  if s[i] == '1' and s[i+1] == '0': count0 += 1    

print(min(count0, count1))
