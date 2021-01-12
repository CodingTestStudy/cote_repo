# 모험가 길드
# n : 모험가의 수 (1 <= n <= 100,000)
# 공포도 값들 입력
n = int(input())
x = list(map(int, input().split()))
x.sort()
count = 0
person = 0
for i in x:
  person += 1
  if i == person:
    person = 0
    count += 1      

print(count)