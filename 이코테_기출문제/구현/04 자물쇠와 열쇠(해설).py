# 2차원 리스트 90도 회전
def rotation_a_matrix_by_90_degree(a):
    n = len(a)  # 행의 길이 계산
    m = len(a[0])  # 열의 길이 계산
    result = [[0] * n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result


# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 전환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 좌물쇠의 중앙 부분에 기존의 좌물쇠 넣기
    for i in range(n):
        for j in range(m):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
        key = rotation_a_matrix_by_90_degree(key)  # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 좌물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                # 새로운 좌물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock):
                    return True
                # 좌물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
if solution(key, lock):
    print("True")
else:
    print("False")
