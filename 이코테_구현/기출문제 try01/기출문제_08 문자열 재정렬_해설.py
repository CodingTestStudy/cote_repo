data = input()
result = []
value = 0

for x in data:
  # 알파벳인 경우 확인 함수
  if x.isalpha():
    result.append(x)
  # 숫자인 경우, 여기서 바로 덧셈
  else:
    value += int(x)

# 오름차순 정렬
result.sort()

# 숫자 존재하면 result 리스트 뒤에 문자열 형태로 추가
if value != 0:
  result.append(str(value))

# 최종 결과 출력
# 리스트를 문자열로 뱐환하여 출력
print(''.join(result))