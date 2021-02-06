import sys

def rotation(n, d): # n : 회전 대상 톱니바퀴 번호, 회전 방향
    if not visited[n]: # 기존에 다룬 적이 없다면
        visited[n] = True # 다룬 적 있다고 처리 후
        left = data[n][6] # 해당 톱니바퀴에서 비교 대상이 될 왼쪽 바퀴
        right = data[n][2] # 해당 톱니바퀴에서 비교 대상이 될 오른쪽 바퀴

        # 해당 톱니바퀴 자체 회전
        if d == 1: # 시계 방향이라면
            temp = data[n][7]
            for i in range(6, -1, -1):
                data[n][i + 1] = data[n][i]
            data[n][0] = temp
        else: # 반시계 방향이라면
            temp = data[n][0]
            for i in range(7):
                data[n][i] = data[n][i + 1]
            data[n][7] = temp

        # 주변 회전 가능한지 확인 후, 회전 함수 재귀 여부 결정
        if n - 1 >= 0 and left != data[n - 1][2]: # 해당 톱니바퀴 왼쪽에 톱니바퀴가 존재하고, 비교 대상이 서로 다른 값이라면
            rotation(n - 1, -d) # 왼쪽 톱니바퀴 회전, 이전과 반대로 회전하기 위해 -d
        if n + 1 <= 3 and right != data[n + 1][6]: # 해당 톱니바퀴 오른쪽에 톱니바퀴가 존재하고, 비교 대상이 서로 다른 값이라면
            rotation(n + 1, -d) # 오른쪽 톱니바퀴 회전, 이전과 반대로 회전하기 위해 -d

data = [] # 톱니바퀴 데이터 저장 리스트
for _ in range(4):
    data.append(list(sys.stdin.readline().strip())) # 톱니바퀴 데이터 입력받음

K = int(input()) # 회전 횟수 입력
for _ in range(K):
    visited = [False] * 4 # 각 회전 할때마다 톱니바퀴 회전 여부 갱신
    number, direction = map(int, sys.stdin.readline().strip().split()) # 톱니바퀴 번호, 방향 입력
    rotation(number - 1, direction) # 실제 인덱스는 0~3이기 때문에 -1 연산

result = 0
for i in range(4):
    if data[i][0] == '1': # i번 톱니바퀴의 S극이면
        result += pow(2, i) # 2의 i 제곱만큼 점수 누적

print(result)

