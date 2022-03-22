from copy import deepcopy


def solution(key, lock):
    lock_home = []
    lock_dolgi = []
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if lock[i][j] == 0:
                lock_home.append([i, j])
            else:
                lock_dolgi.append([i, j])

    if not lock_home:
        return True

    key_dolgi = []
    for i in range(len(key)):
        for j in range(len(key[0])):
            if key[i][j] == 1:
                key_dolgi.append([i, j])

    turning_key = [key_dolgi]
    for step in range(3):
        temp = []
        for i, j in turning_key[-1]:
            temp.append([len(key[0]) - 1 - j, i])
        turning_key.append(temp)
    # print(turning_key)

    # 4가지 방향
    for d in range(4):
        for dd in range(len(turning_key[0])):

            r, c = turning_key[d][dd]
            # lock 대상
            for i in range(len(lock_home)):
                temp_key = deepcopy(turning_key[d])

                move_r = lock_home[i][0] - r
                move_c = lock_home[i][1] - c
                flag = True
                for j in range(len(temp_key)):
                    temp_key[j][0] += move_r
                    temp_key[j][1] += move_c

                    if [temp_key[j][0], temp_key[j][1]] in lock_dolgi:
                        flag = False
                        break
                if not flag:
                    continue

                cnt = 0
                for l in range(len(lock_home)):
                    if lock_home[l] in temp_key:
                        cnt += 1
                        if cnt == len(lock_home):
                            return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
