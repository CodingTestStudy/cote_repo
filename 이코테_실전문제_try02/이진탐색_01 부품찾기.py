# 부품 찾기
# n : 매장 부품 개수 (1 <= n <= 1,000,000)
# m : 부품 요청 개수 (1 <= m <= 1,000,000)

# 이진 탐색(재귀 함수)
def binary_sort(array, target, start, end):  
  if start > end:    
    return "NO"
  mid = (start + end) // 2  
  if array[mid] == target:    
    return "YES"
  elif array[mid] > target:    
    return binary_sort(array, target, start, mid - 1)
  else:  
    return binary_sort(array, target, mid + 1, end)    
  
  
n = int(input())
n_array = list(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))

n_array.sort()

for i in m_array:  
  print(binary_sort(n_array, i, 0, n - 1))


