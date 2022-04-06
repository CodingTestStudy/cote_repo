from collections import deque


# index 0~n-1
def solution(n, stations, w):
    answer = 0
    # 가능 범위 구하고 그 외의 부분 처리하기
    possible = deque()
    impossible = []
    for station in stations:
        station -= 1
        possible.append([max(0, station - w), min(station + w, n - 1)])
    now = 0

    # 전파가 도달하지 않는 범위 찾기
    while possible:
        start, end = possible.popleft()
        if now <= start - 1:
            impossible.append([now, start - 1])

        now = end + 1

    if now < n:
        impossible.append([now, n - 1])

    # 전파 도달 불가 범위를 토대로 계산처리
    elec_length = 1 + 2 * w
    while impossible:
        start, end = impossible.pop()
        length = end - start + 1
        answer += length // elec_length + 1
        if length % elec_length == 0:
            answer -= 1

    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))


# another solution
# index 1~n 기준
def solution(n, stations, w):
    answer = 0
    idx = 0
    location = 1

    # 왼쪽에서부터 w+1만큼씩 이동시키고 확인해가면 진행
    while location <= n:
        # 현재 위치가 기지국 가능 범위 가장 왼쪽보다 뒤에 있다면, 위치 갱신 및 다음 기지국으로 변경
        if idx < len(stations) and location >= stations[idx] - w:
            location = stations[idx] + w + 1
            idx += 1
        # 현재 위치가 기지국 가능 범위 가장 왼쪽보다 앞에 있다면, 기지국 설치 처리 및 다음 위치 갱신
        # 현재 위치에 기지국을 설치하고 해당 기지국 다음에도 기지국이 추가로 존재하기 때문에 2*w+1만큼 이동 처리
        else:
            location += 2 * w + 1
            answer += 1
    return answer
