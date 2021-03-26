import sys
N = int(input())
input_list = []

for _ in range(N):
    d, w = map(int, sys.stdin.readline().strip().split())
    input_list.append((d, w))

input_list.sort()
new_list = [] # 해당 날에 수행할 과제 후보들을 저장할 리스트
result = 0 # 과제 점수 누적합
max_d = input_list[-1][0] # 가장 마지막 마감일

# 마감일 -> 시작날 순서, i번째 날에 수행할 최대 과제 점수 누적
for i in range(max_d, 0, -1):
    while input_list: # 과제가 남아있다면
        # 남은 과제 중, 마감일이 가장 늦은 날이 i 번째 날보다 늦거나 같다면
        if input_list[-1][0] >= i:
            # 해당 과제 점수 new_list 에 저장
            new_list.append(input_list.pop()[1])
        else:
            break

    if new_list:
        new_list.sort()
        # 과제 후보들 중, 가장 큰 과제점수 누적
        result += new_list.pop()
print(result)