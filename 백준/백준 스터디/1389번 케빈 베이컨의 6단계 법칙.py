import sys
N, M = map(int, input().split())
friends = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    friends[a].append(b)
    friends[b].append(a)


def bfs(v):
    count = 0
    for target in range(1, N + 1): # 모든 유저에 대해서
        temp = friends # 리스트 복사
        if target != v: # 연결확인할 유저가 자기자신이 아니라면
            k = 0 # 단계 초기화
            temp_set = set(temp[v]) # v 유저와 연결된 유저들을 저장할 set 함수
            while True:
                k += 1 # k 단계만큼 덧셈 연산할 예정
                pass_list = set() # 다음 단계의 유저들과 추가로 연결된 유저들 옮기기 위한 임시 리스트
                if target in temp_set: # 위에서 설정한 유저 리스트에 target(1~5)가 존재하면
                    count += k # 해당 단계만큼 덧셈 연산 누적
                    break # 다음 연결된 유저로 바꾸기 위해.  target 변경 예정
                else:
                    for value in temp_set: # 연결되어 있는 유저들을
                        pass_list.add(value) # 임의의 리스트에 삽입하고
                    for value in pass_list: # 해당 유저에 대해서
                        for va in temp[value]: # 이어서 연결된 유저들을 추가로 삽입
                            if va != v: # 자기자신이 아니라면
                                temp_set.add(va)
        # v = 1 인 경우를 예로하면
        # 처음 temp_set 에 [2, 3]이 있는 상태이고,
        # 23줄 이후의 반복문들을 통해 2, 3와 연결되어 있는 값들을
        # temp_set에 추가로 삽입한 후, while문 처음으로 돌아가서
        # k(단계) 값을 증가시킨 후, target이 유저가 추가된 리스트(temp_set)에
        # 존재하는지 확인하는 작업 반복
    return count


min_value = int(1e9)
min_index = 0
# count 최솟값 선정 후, 해당 index값 선정 및 출력
for i in range(1, N + 1):
    if min_value > bfs(i):
        min_value = bfs(i)
        min_index = i

print(min_index)
