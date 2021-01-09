# 이진 탐색(반복문)
n = int(input())
n_array = list(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))

n_array.sort()

def binary_sort(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return "yes"
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1

  return "no"

for i in m_array:
  print(binary_sort(n_array, i, 0, n - 1), end=' ')