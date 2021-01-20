n, k = map(int, input().split())
data = list(input())
array = []
count = 0
for i in range(n):  # 0 ~ n - 1 번째 데이터 비교하기
    # 데이터를 삽입하기 전에, 삽입할 데이터와 마지막 데이터와 비교
    while array and array[-1] < data[i] and count < k:
        array.pop()
        count += 1
    array.append(data[i])

# ex) 7654321 인 경우, 값이 삽입될 때마다, 이전의 값이 더 크기 때문에
# 위의 for문에서 빠지지 않고 남아있다.
for _ in range(k - count):
    array.pop()

for value in array:
    print(value, end='')
