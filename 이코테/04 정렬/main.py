n = int(input())

array = []
for i in range(n):
  input_data = input().split()
  # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
  array.append((input_data[0], int(input_data[1])))

# 키를 이용하여, 점수를 기준으로 정렬
# 람다 함수 사용하자
array = sorted(array, key=lambda stduent: stduent[1])

for stduent in array:
  print(stduent[0], end=' ')