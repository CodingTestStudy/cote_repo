import sys
from collections import deque
T = int(input()) # 테스트 케이스 1 <= T <= 100
result = []

def delete(array): # 리스트 내의 문자를 지울 수 있는지 확인하는 함수
    if len(array) == 0 or array[0] == '': return False # 리스트가 비어있는 경우
    else: return True

for _ in range(T):
    p = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    x = sys.stdin.readline().strip('[]\n').split(',')
    x = deque(x)

    count = 0 # 최종 값이 짝수면 그대로, 홀수면 뒤집기
    flag = 1 # 1이면, popleft(), -1이면 pop()으로 값 빼기
    for value in p:
        if value == 'R':
            flag = -flag
            count += 1
        elif value == 'D':
            if delete(x): # 리스트내의 데이터를 지울 수 있는 경우
                if flag == 1:
                    x.popleft()
                elif flag == -1:
                    x.pop()
            else: # 지울 수 있는 데이터가 없는 경우
                x = ["error"]
                break

    if count % 2 == 1 and len(x) > 0: x.reverse() # 뒤집을 수 있는 경우
    # 아래의 if 문을 합칠 수 없다.
    # len(x) >= 0 으로 조건문을 합치면, len(x) = 0 일 때, x[0]가 불가능하므로, 인덱스 에러 발생
    if len(x) > 0 and x[0] != "error":
        x.appendleft("["), x.append("]")
    if len(x) == 0:
        x.appendleft("["), x.append("]")
    result.append(x) # 각 테스트 케이스의 최종 결과를 result 리스트에 삽입

for value in result: # 각 테스트 케이스에서 만들어진 문자열들에 대해서
    for i in range(len(value)):
        if i == 0 or i == len(value) - 2 or i == len(value) - 1: # ','가 필요 없는 index
            print(value[i], end='')
        else: # ','가 필요한 index
            print(value[i], end=',')
    print()
