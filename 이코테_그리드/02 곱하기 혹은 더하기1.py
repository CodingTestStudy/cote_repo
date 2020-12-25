# 02984 -> 576
import time

# 정수 문자열 입력
number = input()
# 시간 측정
start = time.time()
number_list = []
result = 0
for i in range(len(number)):
  number_list.append(number[i])

for i in range(len(number_list) - 1):
  if number_list[i] == "0" or number_list[i+1] == "0":
    result = int(number_list[i]) + int(number_list[i+1])
  else:
    result = int(number_list[i]) * int(number_list[i+1])
  number_list[i+1] = result
  
print(result)
print(time.time()-start)
