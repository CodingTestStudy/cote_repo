n, m = map(int, input().split())
card = [list(map(int, input().split())) for _ in range(n)]  # 행렬 입력 받음
result = 0
for i in range(n):
  card[i].sort()  # 오름차순을 정렬

for i in range(n - 1):
  result = max(card[i][0], card[i+1][0])  # 각 행렬값의 첫 번째 요소들 비교

print(result)  