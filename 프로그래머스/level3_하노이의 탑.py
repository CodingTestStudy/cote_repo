def hanoi(count, start, to, mid, answer):
    if count == 1:
        return answer.append([start, to])
    # 1번 기둥에 있는 n개의 원반 중 n-1개를 2번 기둥으로 옮김(3번 기둥 거치면서)
    hanoi(count - 1, start, mid, to, answer)
    # 1번 기둥에 남아있는 가장 큰 원반을 3번으로 옮김
    answer.append([start, to])
    # 2번 기둥에 있는 n-1개의 원반을 다시 3번 기둥으로 옮김(1번 기둥 거치면서)
    hanoi(count - 1, mid, to, start, answer)


def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer

print(solution(4))
