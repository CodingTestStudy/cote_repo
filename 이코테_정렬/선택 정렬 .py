# 선택 정렬 
# N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보냄
# N + (N - 1) + (N - 2) + ... + 2
# (N^2 + N - 2) / 2
# 시간 복잡도 : O(N^2) 

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i # 가장 작은 원소의 인덱스
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j

  array[i], array[min_index] = array [min_index], array[i] # swap

print(array)