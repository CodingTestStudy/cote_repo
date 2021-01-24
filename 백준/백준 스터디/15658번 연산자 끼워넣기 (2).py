N = int(input())
data = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

max_result = -int(1e9) # 최대값 초기화, 앞으로 갱신될 어떠한 값보다 작아야 하기 때문에, 극단적인 값으로 초기화함
min_result = int(1e9) # 최소값 초기화, 앞으로 갱신될 어떠하 값보다 커야하기 때문에, 극단적인 값으로 초기화함

def rotation(index, result):
    global max_result, min_result
    if index == N: # N번 연산을 완료했다면
        max_result = max(max_result, result) # 최대값과 비교후 갱신 여부 결정
        min_result = min(min_result, result) # 최소값과 비교 후 갱신 여부 결정
        return

    if op[0] > 0: # 덧셈 연산 횟수가 남아있다면
        op[0] -= 1 # 덧셈 연산 횟수 감소 후
        rotation(index + 1, result + data[index]) # 덧셈 연산을 하는 재귀 함수
        op[0] += 1 # 나중에 또 연산을 수행하기 위해 연산 횟수 복구
    if op[1] > 0:
        op[1] -= 1
        rotation(index + 1, result - data[index])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        rotation(index + 1, result * data[index])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        rotation(index + 1, int(result/data[index]))
        op[3] += 1


rotation(1, data[0]) # 1~N 으로 N번 연산하기 위해 index를 1로 설정
print(max_result)
print(min_result)