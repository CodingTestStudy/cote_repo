# 팀 결성
n, m = map(int, input().split()) # 번호, 연산 횟수 입력

team = [[] for _ in range(n + 1)]
result = []
for i in range(n + 1):
  team[i] = i


def find_team(team, x):
  if team[x] != x:
    team[x] = find_team(team, team[x])
  return team[x]

def union_team(team, a, b):
  a = find_team(team, a)
  b = find_team(team, b)
  if a < b:
    team[b] = a
  else:
    team[a] = b

for _ in range(m):
  a, b, c = map(int, input().split())
  if a == 0:
    union_team(team, b, c)    
  else:
    if find_team(team, b) == find_team(team, c):     
      result.append("YES")
    else:      
      result.append("NO")

for result in result:
  print(result)
