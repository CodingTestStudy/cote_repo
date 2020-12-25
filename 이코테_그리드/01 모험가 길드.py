# 5
# 2 3 1 2 2 -> 2

# 정렬 생각하기

n = int(input())
person = list(map(int, input().split()))
person.sort()

result = 0 # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in person:  # 공포도를 낮은 것부터 하나씩 확인하며
  count += 1 # 그룹에 모험가 추가
  if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1 # 총 그룹의 수 증가
    count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result)
