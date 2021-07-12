# 못푼 문제, 백트래킹, 가지치기

def check(start, nxt, n, col):
    for i in range(start):
        # 같은 라인에 있거나, 대각선에 존재하는 경우
        # 퀸이 존재할 수 없는 경우임
        if nxt == col[i] or abs(nxt - col[i]) == start - i:
            return False
    return True


def queen(start, n, col):
    # 마지막까지 확인한 경우
    # 즉, 퀸이 n개 자리가 가능한 경우를 찾았을 때
    # count += 1이 됨
    if start == n:
        return 1

    count = 0
    for nxt in range(n):
        # 다음 퀸을 놓을 수 있는 경우
        if check(start, nxt, n, col):
            col[start] = nxt
            count += queen(start + 1, n, col)
    return count


def solution(n):
    col = [0] * n
    start = 0
    return queen(start, n, col)


print(solution(4))
