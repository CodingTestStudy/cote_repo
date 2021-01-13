n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
# 0~10 무게를 담는 리스트
array = [0] * 11

# 리스트에 각 공의 무게의 개수 저장
for x in data:
  array[x] += 1

count = 0
for i in range(1, m + 1):
  # i 는 무게
  n -= array[i] # 남은 개수에서 현재 무게의 공 개수 빼기
  count += n * array[i] # 남은 개수만큼 현재의 공 개수 곱함

print(count)