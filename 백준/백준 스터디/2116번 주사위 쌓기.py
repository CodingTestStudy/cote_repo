import sys
import copy
N = int(input()) # 주사위 개수 입력
dice = [] # 주사위 데이터 리스트
result = [] # 첫 번째 주사위의 bottom 값 (1~6) 에 대한 결과들을 저장하는 리스트
for _ in range(N):
    dice.append(list(map(int, sys.stdin.readline().strip().split())))

# now 번째 주사위의 top 값을 return 하고, bottom 값을 0으로 초기화해주는 함수
# bottom 값을 0으로 초기화해주는 이유는 어차피 옆면의 숫자만 비교, 계산하기 때문
def process(array, now, idx): # idx : 주사위의 bottom 에 해당하는 index
    now_top = 0
    if idx == 0:
        now_top = array[now][5] # top 저장
        array[now][0] = 0 # bottom 0으로 초기화
    elif idx == 1:
        now_top = array[now][3]
        array[now][1] = 0
    elif idx == 2:
        now_top = array[now][4]
        array[now][2] = 0
    elif idx == 3:
        now_top = array[now][1]
        array[now][3] = 0
    elif idx == 4:
        now_top = array[now][2]
        array[now][4] = 0
    elif idx == 5:
        now_top = array[now][0]
        array[now][5] = 0
    return now_top # now 번째 주사위에서의 top

# top 값을 0으로 초기화해주는 함수를 따로 만들어준 이유는
# 만약 위의 process 함수에서 top 값도 같이 0으로 초기화해주면,
# 다음 주사위의 bottom 값을 찾는데 top 값이 0으로 초기화 되어있어서, bottom 값을 찾을 수 없다.
def delete_top(array, idx, value):
    for i in range(6): # 모든 주사위 면에 대해서
        if array[idx][i] == value: # 해당 면의 값이 top 값이라면
            array[idx][i] = 0 # 해당 면 0으로 최기화
            break

for i in range(6):
    temp = copy.deepcopy(dice) # 기존의 주사위 복사, 앞의 과정에서 값들이 바뀌기 때문
    top = process(temp, 0, i) # 첫 번째 주사위 처리
    for j in range(1, N):
        delete_top(temp, j - 1, top) # 이전의 주사위의 top 값을 0으로 초기화
        for k in range(6): # 주사위의 모든 면에 대해서
            if temp[j][k] == top: # j 번째 주사위에서 top 값과 동일한 k면에 대해서
                top = process(temp, j, k) # 이전의 주사위의 top 값(k면)을 0으로 초기화
                break
    delete_top(temp, N - 1, top) # 마지막 주사위의 top 값도 0으로 초기화
    answer = 0
    for x in range(N):
        answer += max(temp[x]) # 각 데이터읭 최댓값들을 덧셈한 후,
    result.append(answer) # 해당 결과값들을 결과 리스트에 저장

print(max(result)) # 결과 리스트에서 최댓값 출력
