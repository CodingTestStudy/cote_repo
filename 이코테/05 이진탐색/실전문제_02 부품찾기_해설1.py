# 이진 탐색 소스코드 구현 (반복문)
# 이전의 나의 코드는 재귀적 표현 (함수 반복)
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 변환
    if array[mid] == target:
      return mid
    # 중간점의 값보다 찾고자 하는 값이 작으면 왼쪽 확인
    elif array[mid] > target:
      end = mid - 1
    else:
    # 중간점의 값보다 찾고자 하는 값이 크면 오른쪽 확인
      start = mid + 1
  return None

n = int(input())
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 위해 사전에 정렬 수행

m = int(input())
x = list(map(int, input().split()))

for i in x:
  result = binary_search(array, i, 0, n - 1)
  if result != None:
    print('yes', end=' ')
  else:
    print('no', end=' ')



