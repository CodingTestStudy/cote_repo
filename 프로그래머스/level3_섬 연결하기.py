def solution(n, costs):
    answer = 0
    # 가격 순으로 정렬
    costs = sorted(costs, key=lambda x: x[2])
    # 연결된 섬 저장하기 위한 set함수
    connected = set()
    connected.add(0)

    # n개의 섬이 set함수에 모두 들어갈 때까지 반복
    while len(connected) != n:
        for cost in costs:
            d1, d2, c = cost
            if d1 in connected or d2 in connected:
                # 2개의 섬이 모두 set함수에 포함되어 있다면,
                # 이전에 다룬 섬들이므로 pass
                if d1 in connected and d2 in connected:
                    pass
                # 그렇지 않다면, 해당 섬들 set함수에 삽입
                else:
                    connected.add(d1)
                    connected.add(d2)
                    answer += c
                    break
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
