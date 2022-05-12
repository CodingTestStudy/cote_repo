from itertools import combinations
from copy import deepcopy

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


# 궁수와 적의 거리 계산
def calc_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


# 궁수가 적 공격 가정
def attack(temp, r, c, attack_list):
    # 공격당하는 적 리스트
    test = []

    # (r, c) -> 궁수 위치
    # 궁수와 가까은 행에서부터 검사
    for i in range(r - 1, -1, -1):
        for j in range(M):
            if temp[i][j] == 1:
                distance = calc_distance(r, c, i, j)
                if distance <= D:
                    test.append((distance, j, i))
    # 공격 받은 적 중에서, 궁수와 가장 가깝고, 그 중에 왼쪽에 있는 적 선정
    if test:
        test.sort()
        target = test[0]
        attack_list.append((target[2], target[1],))
        return True
    return False


answer = 0
cnt = 0
# 3명의 궁수 위치의 경우의 수
for archer in combinations([i for i in range(M)], 3):
    result = 0
    attack_list = []
    temp = deepcopy(board)
    for r in range(N, 0, -1):
        for c in archer:
            # 3명의 궁수 공격
            if cnt < 3:
                if attack(temp, r, c, attack_list):
                    cnt += 1
        cnt = 0
        # 공격 당한 적의 수 카운트
        for rr, cc in attack_list:
            if temp[rr][cc] == 1:
                result += 1
                temp[rr][cc] = 0
    if answer < result:
        answer = result
print(answer)
