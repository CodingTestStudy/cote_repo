# 반례 존재

# 가장 앞의 단어인 A에 9를 할당하는 경우가 항상 가장 큰 경우가 아니다.
import heapq
import sys

N = int(input())
data = []
# 26개의 알파벳 각각 위치의 값을 10으로 초기화 (10이면 값이 변하지 않았음을 의미)
# 값을 할당할 때 위, 아래 방향으로 2번 할당해서 합이 더 큰 값을 추리기 위해 2번 반복해서 생성
visited = [[10] * 26 for _ in range(2)]
q = []
sum_value = 0
for i in range(N):
    x = list(sys.stdin.readline().rstrip())
    data.append(x)
    heapq.heappush(q, -len(x))  # 단어의 길이가 가장 긴 데이터를 찾기 위해 우선순위 큐 사용

first_max_length = -heapq.heappop(q)    # 가장 긴 단어의 길이
second_max_length = -heapq.heappop(q)   # 두번째로 긴 단어의 길이
dif = first_max_length - second_max_length  # 해당 부분은 다른 단어와 겹치는 경우가 없기 때문에, 해당 부분은 가장 큰 값 지정하고자했음

# print("first_max_length : ", first_max_length)
# print("second_max_length : ", second_max_length)

# 입력받은 각각의 데이터 중에서 길이가 가장 긴 데이터의 순서를 찾음
idx = 0
for i in range(N):
    if len(data[i]) > len(data[idx]):
        idx = i


# 앞에서부터 가장 큰 값 할당
for i in range(dif):
    # print(ord(data[idx][0]), 9 - i)
    visited[0][ord(data[idx][0]) - 65] = 9 - i  # 알파벳 리스트에 해당 알파벳 위치에 값 갱신
    visited[1][ord(data[idx][0]) - 65] = 9 - i  # 알파벳 리스트에 해당 알파벳 위치에 값 갱신
    sum_value += (9 - i) * 10 ** (first_max_length - i - 1) # 값 축적
    # print(data[idx][0], "삭제")
    del data[idx][0]    # 계산 완료한 부분 삭제


# case1
start_num = min(visited[0]) # 위에서 할당한 값 제외, 가장 큰 값 찾기
rest_sum1 = 0
for i in range(second_max_length):
    for j in range(N):
        if visited[0][ord(data[j][i]) - 65] >= 10:  # 해당 알파벳이 값을 할당받지 않았다면
            start_num -= 1
            visited[0][ord(data[j][i]) - 65] = start_num    # 남은 수 중 가장 큰 값 할당
            # print(data[j][i], "->", start_num)
            # print(start_num * (10 ** (second_max_length - 1 - i)))
            rest_sum1 += start_num * (10 ** (second_max_length - 1 - i))    # 값 축적
        else:
            rest_sum1 += visited[0][ord(data[j][i]) - 65] * (10 ** (second_max_length - 1 - i)) # 이미 할당받은 값을 토대로 값 축적

# case2
start_num = min(visited[1])
rest_sum2 = 0
for i in range(second_max_length):
    for j in range(N - 1, -1, -1):
        if visited[1][ord(data[j][i]) - 65] >= 10:
            start_num -= 1
            visited[1][ord(data[j][i]) - 65] = start_num
            # print(data[j][i], "->", start_num)
            # print(start_num * (10 ** (second_max_length - 1 - i)))
            rest_sum2 += start_num * (10 ** (second_max_length - 1 - i))
        else:
            rest_sum2 += visited[1][ord(data[j][i]) - 65] * (10 ** (second_max_length - 1 - i))

# print(rest_sum1)
# print(rest_sum2)

print(sum_value + max(rest_sum1, rest_sum2))
