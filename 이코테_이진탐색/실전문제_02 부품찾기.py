# 부품 찾기
# 이진 탐색 알고리즘 사용
# 재귀적 구현
# 이진 탐색을 위해 오름차순으로 미리 정렬해야함
n = int(input())
array1 = list(map(int, input().split()))
array1.sort()
m = int(input())
array2 = list(map(int, input().split()))

start = 0
end = n - 1

def binary_search(array1, target, start, end):
  if len(array1) <= 1:
    return None
  if start > end:
    return 'no'
  mid = (start + end) // 2
  if array1[mid] == target:
    return 'yes'
  elif array1[mid] >= target:
    return binary_search(array1, target, start, mid - 1)
  else:
    return binary_search(array1, target, mid + 1, end)
  

for i in range(m):
  result = binary_search(array1, array2[i], start, end)
  print(result, end=' ')