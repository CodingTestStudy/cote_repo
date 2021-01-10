# 떡뽁이 떡 만들기
# n : 떡의 개수 (1 <= n <= 1,000,000)
# m : 떡의 길이 (1 <= m <= 2,000,000,000)
n, m = map(int, input().split())
dduk = list(map(int, input().split()))
result = 0

def binary_sort(dduk, start, end):    
  while start <= end:        
    total = 0    
    mid = (start + end) // 2
    for value in dduk:
      if value >= mid:        
        total += value - mid               
    
    if total < m:
      end = mid - 1
    else:
      result = mid
      start = mid + 1
      
  return result
    
dduk.sort()

print(binary_sort(dduk, 0, max(dduk)))