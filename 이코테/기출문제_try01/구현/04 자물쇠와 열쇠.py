# 자물쇠와 열쇠
# 73.0 / 100.0 테스트 케이스는 통과했지만,  채점시 오답 케이스들 몇몇 존재
import copy
rotation_time = 0


def make_new_lock(lock):
    lock_data = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 1:
                lock_data.append((i + len(lock), j + len(lock)))

    lock_size = len(lock)**2
    new_lock = [[0] * lock_size for _ in range(lock_size)]
    for value in lock_data:
        i, j = value
        new_lock[i][j] = 1

    return new_lock


def rotation_key(key):
    new_key = copy.deepcopy(key)
    for i in range(len(key)):
        for j in range(len(key)):            
            new_key[j][i] = key[len(key) - 1 - i][j]

    return new_key


def solution(key, lock):
    l = make_new_lock(lock)
    global rotation_time    

    test_matrix = [[1] * (len(key)) for _ in range(len(key))]
    for i in range(len(l) - len(lock) + 1):
        for j in range(len(l) - len(lock) + 1):
            count1 = -1
            for x in range(i, i + len(key)):
                count1 += 1
                count2 = -1
                for y in range(j, j + len(key)):
                    count2 += 1
                    test_matrix[count1][count2] = l[x][y]
                    
            result = []
            for a in range(len(key)):
                for b in range(len(key)):
                    result.append(key[a][b] + test_matrix[a][b])
          
            for value in result:
                if value != 1:
                    break
                else:
                    return True

    if rotation_time == 4:
        return False
    else:
        rotation_time += 1
        solution(rotation_key(key), lock)    


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
if solution(key, lock):
    print("True")
else:
    print("False")
