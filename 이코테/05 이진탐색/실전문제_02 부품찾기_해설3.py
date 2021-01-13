# 집합 자료형 정렬 사용
n = int(input())
array1 = list(map(int, input().split()))
array1.sort()

m = int(input())
array2 = list(map(int, input().split()))

for i in array2:
  if i in array1:
    print('yes', end=' ')
  else:
    print('no', end=' ')
