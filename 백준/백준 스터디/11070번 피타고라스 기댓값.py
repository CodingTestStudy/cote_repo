import sys
T = int(input()) # 테스트 케이스 개수
answer = [] # 각 테스트 케이스에서의 최대 기댓값, 최소 기댓값 순서로 입력받는 리스트
for _ in range(T):
    testcase = [] # 현재 테스트 케이스에서 각 팀의 기댓값을 갖는 리스트
    N, M = map(int, sys.stdin.readline().rstrip().split()) # 팀 개수, 전체 경기 수
    graph = [[0, 0] for _ in range(N + 1)] # 첫 번째 인덱스는 득점, 두 번째 인덱스는 실점

    for _ in range(M):
        a, b, p, q = map(int, sys.stdin.readline().rstrip().split())
        graph[a][0] += p # a의 득점
        graph[a][1] += q # a의 실점
        graph[b][0] += q # b의 득점
        graph[b][1] += p # b의 실점

    W = 0
    for i in range(1, N + 1):
        if graph[i][0] == 0 and graph[i][1] == 0: # 문제 조건에서 총 득점, 실점 이 모두 0이라면 기댓값 0이라고 지정
            W = 0
        else: # 그렇지 않은 경우, 기댓값 계산
            W = (1000 * graph[i][0] ** 2 // (graph[i][0] ** 2 + graph[i][1] ** 2))

        testcase.append(W) # 위에서 만든 기댓값을 리스트에 삽입
    answer.append(max(testcase)) # 현재 테스트 케이스에서 받은 기댓값 중, 최댓값을 정답 리스트에 삽입
    answer.append(min(testcase)) # 현재 테스트 케이스에서 받은 기댓값 중, 최솟값을 정답 리스트에 삽입

for value in answer: # 정답 리스트에 저장된 값들을 차례대로 출력
    print(value)
