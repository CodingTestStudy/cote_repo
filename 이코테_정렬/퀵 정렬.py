# 퀵 정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준(Pivot)으로 설정
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: # 원소가 1개인 경우 종료
   return

  pivot = start # 피벗은 첫 번째 원소
  left = start + 1
  right = end
  while (left <= right):
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while(left <= end and array[left] <= array[pivot]):
      left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while(right > start and array[right] >= array[pivot]):
      right -= 1

    # 엇갈렸다면 작은 데이터와 피벗을 교체
    if (left > right):
      array[right], array[pivot] = array[pivot], array[right]
    # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
    else:
      array[left], array[right] = array[right], array[left]

  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right -1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)



# 퀵 정렬의 시간 복잡도
# 평균 : O(NlogN)
# 최악 : O(N^2), 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해서 퀵 정렬을 수행하면 최악, 모든 수에 대해서 분할을 해줘야 하기 때문에