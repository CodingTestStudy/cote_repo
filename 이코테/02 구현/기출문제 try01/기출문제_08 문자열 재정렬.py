# 문자열 재정렬
# 'A' ~ 'Z' = 65 ~ 90
# '0' ~ '9' = 48 ~ 57
import time

data = list(input())
start = time.time()
alphabet_num = []
number = []
alph = ''
result = 0

for i in range(len(data)):  
  if 65 <= ord(data[i]) <= 90:
    alphabet_num.append(ord(data[i]))
  elif 48 <= ord(data[i]) <= 57:
    number.append((data[i]))

alphabet_num.sort()
for i in alphabet_num:
  alph += chr(i)   

for i in number:
  result += int(i)

print(alph + str(result))
print(time.time() - start)

