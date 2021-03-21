import sys

month = [0] * 13
month[2] = 31
set30 = [5, 7, 10, 12]
set31 = [4, 6, 8, 9, 11]
for i in range(13):
    if i > 2:
        if i == 3: month[i] += month[i - 1] + 28
        elif i in set31: month[i] += month[i - 1] + 31
        elif i in set30: month[i] += month[i - 1] + 30
flowers = [] # 입력받은 꽃들의 피고지는 날짜를 저장할 리스트
# 공주가 좋아하는 계절
princess_start = month[3] + 1
princess_end = month[11] + 30

N = int(input())
for _ in range(N):
    x, y, z, r = map(int, sys.stdin.readline().strip().split())
    flowers.append((month[x] + y, month[z] + r))
flowers.sort()
end = princess_start
k = -1
temp = 0
selected = [] # 선택된 꽃 저장 리스트
# 지는 시간이 피는 시간보다 늦고, 탐색할 꽃이 더 존재한다면
while end <= princess_end and k < N:
    change = False
    k += 1 # 다음 꽃 확인
    for i in range(k, N):
        if flowers[i][0] > end: # 피는 시간이 지는 시간보다 늦다면
            break
        if temp < flowers[i][1]: # 이전 꽃보다 지금 꽃이 더 늦게 진다면
            temp = flowers[i][1] # 지는 시간 갱신
            time = i # 범위내의 가장 늦게 지는 꽃을 기준으로 k 갱신
            change = True # 변화 확인
    if change: # 변화가 존재했다면
        end = temp # 갱신했던 지는 시간으로 end 갱신, while문 조건문에서 사용됨
        selected.append(flowers[k]) # 해당 꽃 저장
    else: # 변화 없었으면
        selected = [] # 꽃 초기화
        break
print(len(selected))