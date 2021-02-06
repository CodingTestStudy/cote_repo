import heapq
N, M = map(int, input().split())
book = list(map(int, input().split()))
plus = []
minus = []
for value in book: # 입력받은 값들에 대해서 양수, 음수 리스트 분리해서 저장
    if value > 0: heapq.heappush(plus, -value)
    else: heapq.heappush(minus, value)


def calc():
    destination = 0 # result에 덧셈으로 계속 갱신해주는 거리 값들
    result = 0 # 최종 거리값
    min_plus_value = 0 # plus 리스트 내에서 가장 작은 값(최대 절댓값)
    min_minus_value = 0 # minus 리스트 내에서 가장 작은 값(최대 절댓값)

    # 리스트에 데이터가 존재할 경우, 각 리스트에서의 최대 절댓값을 구한다
    # 최대 절댓값을 구하는 이유는 최장 거리는 마지막으로 한번만 가는 것이 이득이기 때문
    # 리스트 내에서 가장 작은 값이 최대 절댓값이다. plus 리스트도 삽입할 때, -를 붙여서 삽입했기 때문
    if len(plus) != 0: min_plus_value = -min(plus)
    if len(minus) != 0: min_minus_value = -min(minus)

    # 1. 양수 존재하지 않고, 음수만 존재할 경우
    if len(plus) == 0 and len(minus) != 0:
        destination = min_minus_value # 가장 멀리 있는 값을 도착지로 저장
        if len(minus) >= M: # 현재 남아있는 책의 개수가 최대 들수 있는 개수 이상이라면
            for _ in range(M):
                heapq.heappop(minus) # M개 만큼 뺸다. (destination 으로 갈 때, 같이 들고가기 때문에 들릴 필요 없는 좌표)
        else: return destination # 그렇지 않으면, destination 으로 가는 것이 마지막이기 때문에, destination 만 리턴

    # 2. 음수 존재하지 않고, 양수만 존재할 경우
    elif len(plus) != 0 and len(minus) == 0:
        destination = min_plus_value
        if len(plus) >= M:
            for _ in range(M):
                heapq.heappop(plus)
        else: return destination

    # 3. 양수의 최대 절댓값이 더 큰 경우
    elif min_plus_value > min_minus_value:
        destination = min_plus_value # 양수 최대 절댓값이 도착지로 지정
        if len(plus) >= M: # 남은 책이 M 이상이면
            for _ in range(M):
                heapq.heappop(plus) # M만큼 뺀다. 도착지점 갈 때, 같이 들고가서 다시 올 일이 없기 때문
        else:
            for _ in range(len(plus)): # 남은 책이 M 보다 적으면
                heapq.heappop(plus) # 남아 있는 책 좌표 모두 뺀다.

    # 4. 음수의 최대 절댓값이 더 큰 경우
    elif min_plus_value < min_minus_value:
        destination = min_minus_value
        if len(minus) >= M:
            for _ in range(M):
                heapq.heappop(minus)
        else:
            for _ in range(len(minus)):
                heapq.heappop(minus)

    # 1. 양수 리스트 내의 거리들 계산
    while plus:
        x = 2 * -heapq.heappop(plus) # 가장 멀리 있는 좌표 왔다갔다
        result += x # 그 만큼 최종 걸음에 더해준다.
        if len(plus) >= M - 1:
            for _ in range(M - 1):
                heapq.heappop(plus)
        else:
            for _ in range(len(plus)):
                heapq.heappop(plus)

    # 2. 음수 리스트 내의 거리들 계산
    while minus:
        x = 2 * -heapq.heappop(minus)
        result += x
        if len(minus) >= M - 1:
            for _ in range(M - 1):
                heapq.heappop(minus)
        else:
            for _ in range(len(minus)):
                heapq.heappop(minus)

    result += destination
    return result

print(calc())
