# 수의 개수가 500개 이하로 매우 적다
# 1이상 100,000 이하이므로 어떤 정렬 알고리즘을 사용해도 상관 x

n = int(input())
# n개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
  array.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

# 정렬이 수행된 결과를 출력
for i in array:
  print(i, end=' ')