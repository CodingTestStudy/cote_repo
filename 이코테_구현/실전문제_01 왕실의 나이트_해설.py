# 기존 코드와 방식은 같으나,
# 리스트 활용부분에서 차이가 존재
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# int(ord(?)) int형으로 변환한 이유는?
# type 검사를 했을 때, print(type(ord(?))) -> int가 나옴

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1,2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)