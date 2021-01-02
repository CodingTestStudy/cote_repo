# 모험가 길드
# 입력 : 5 (모험가의 수)
# 입력 : 2 3 1 2 2 (각 모험가의 공포도 값)
# 출력 : 2 (그룹의 최댓값)

n = int(input())  # 모험가 n명 입력
x = list(map(int, input().split())) # 각각의 공포도 입력받음
group = 0 # 그룹 개수
count = 0 # 현재 그룹 내의 멤버 수
x.sort()  # 오름차순으로 정렬, 공포도가 낮은 인원부터 그룹으로 만들어 놓아야 최대한 많은 그룹을 만들 수 있다. 

# 1 2 2 2 3
for i in x:
  count += 1
  if i <= count:
    group += 1
    count = 0
    
print(group)
     

