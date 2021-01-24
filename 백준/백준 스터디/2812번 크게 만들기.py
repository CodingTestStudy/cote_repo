n, k = map(int, input().split())
data = list(input())
array = [] # 가장 큰 수를 만들기 위한 별도의 리스트
count = 0
for i in range(n):  # 0 ~ n - 1 번째 데이터 비교하기
    # array 리스트에 데이터를 삽입하기 전에, 삽입할 데이터와 마지막 데이터와 비교
    # 앞으로 삽일될 데이터가 array 리스트의 맨뒤의 데이터값보다 크다면
    # array 리스트의 맨뒤의 값은 더 작은 값이 존재하는 것을 의미하므로 제거
    while array and array[-1] < data[i] and count < k:
        array.pop()
        count += 1
    # 모든 data 값들이 array 리스트에 삽입되기는 하지만, 뒤에 본인보다 큰 값이 들어오면 삭제됨
    array.append(data[i])

# ex) 7654321 인 경우, 값이 삽입될 때마다, 이전의 값이 더 크기 때문에
# 위의 for 문에서 제거되지 못하고 남아있다.
# 결국엔 그만큼 맨뒤에 있는 값들은 가장 작은값들이므로, 맨뒤의 값들 삭제
for _ in range(k - count):
    array.pop()

for value in array:
    print(value, end='')
