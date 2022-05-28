T = 10


def check_range(i, n):
    if i < 0 or i >= n:
        return False
    return True


def compare(target, nxt):
    if target <= nxt:
        return False
    return True


for idx in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    answer = 0
    for i in range(N):
        flag = True
        result = 0
        for j in [-2, -1, 1, 2]:
            # 범위 확인
            if check_range(i + j, N):
                if compare(data[i], data[i + j]):
                    result = max(result, data[i + j])
                else:
                    flag = False
                    break
        if flag:
            answer += data[i] - result
    print(f"#{idx} {answer}")
