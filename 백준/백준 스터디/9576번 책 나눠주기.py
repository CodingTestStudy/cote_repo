import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    visited = [False] * (N + 1) # 책 대여 여부 확인
    request = [] # 입력받은 책 저장하는 리스트
    for i in range(1, M + 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        request.append((a, b))
    # 책 번호의 마지막 번호가 작은 순서대로 정렬
    request.sort(key=lambda x: x[1])

    count = 0
    while request: # 입력받은 모든 책에 대해서
        start, end = request.pop(0)
        for i in range(start, end + 1):
            if not visited[i]:
                visited[i] = True
                count += 1
                break
    print(count)
