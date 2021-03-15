N = int(input())
data = list(map(int, input().split()))
visited = [0] * N # 줄 순서 초기화(모두 비어있음)
for i in range(1, N + 1):
    x = data[i - 1] # 왼쪽에 i보다 큰 값의 개수
    count = 0 # i보다 큰 개수 (0개부터 탐색 시작)
    for j in range(N):
        # count, x값이 같고 j번째 위치가 비어있다면
        if count == x and visited[j] == 0:
            visited[j] = i
            break
        # count, x값이 같진 않고 j번째 위치가 비어있다면
        # x와 다시 비교하기 위해 count값 증가
        elif visited[j] == 0:
            count += 1
        # j번째에 i가 들어가지 못했을 경우, j+1번째 위치가 적절한지
        # 반복문을 통해 다시 확인

for value in visited:
    print(value, end=' ')
