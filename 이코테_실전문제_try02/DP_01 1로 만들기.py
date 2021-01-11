# 1로 만들기
# (1 <= x <= 30,000)

x = int(input())
x_list = [0] * (x + 1)
count = 1
while count < x:
  count += 1
  x_list[count] += x_list[count - 1] + 1
  if count % 5 == 0:
    x_list[count] = min(x_list[count], x_list[count // 5] + 1)
  elif count % 3 == 0:
    x_list[count] = min(x_list[count], x_list[count // 3] + 1)
  elif count % 2 == 0:
    x_list[count] = min(x_list[count], x_list[count // 2] + 1)   
print(x_list[x])