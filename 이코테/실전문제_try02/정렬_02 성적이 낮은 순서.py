# 성적이 낮은 순서로 학생 출력하기
# n : 학생 수, 1 <= n <= 100,000
# 학생 이름, 점수
n = int(input())
array = []
for _ in range(n):
  array.append(list(input().split()))

array.sort(key=lambda a : a[1])

for i in array:
  print(i[0], end=' ')