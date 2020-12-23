# list comprehension : 기존의 코드보다 간결하게 만들 수 있다.

# 일반적인 코드
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)


# 0~9의 수를 갖는 리스트
array = [i for i in range(10)]
print(array)


# 0~19의 수 중에 홀수만 갖는 리스트
odd_array = [i for i in range(20) if i % 2 == 1]
print(odd_array)


# 1~9의 수들의 제곱 값을 갖는 리스트
squared_array = [i * i for i in range(1, 10)]
print(squared_array)


# 2차원 리스트를 초기화할 떄 효과적으로 사용된다.
# for문 안에서 변수값에 변화를 주지 않고,
# 단순히 반복 수행만을 할 때, _(언더바)를 사용한다.
row = 4
col = 3
array = [[0] * col for _ in range(row)]
print(array)

