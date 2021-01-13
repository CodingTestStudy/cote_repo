# 효율적인 방법
n, m, k = map(int, input().split())
number = list(map(int, input().split()))
number.sort(reverse=True)

a = number[0] # 가장 큰 값
b = number[1] # 그 다음 큰 값

count = m // (k + 1)  # (k * a + b) -> 반복되는 수열을 곱하는 횟수
x = m % (k + 1) # 수열들을 곱하고 수열의 형태가 깨진 후의 나머지 횟수 -> a를 x번 더해주면 된다.
result = 0
result += (k * a + b) * count + a * b
print(result)
