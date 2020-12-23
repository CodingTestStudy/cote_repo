# 람다 표현식
# 특정한 기능을 수행하는 함수를 한 줄에 작성 가능

def add(a, b):
    return a + b


# add() 사용
print(add(1, 2))

# 람다 표현식 사용
print((lambda a, b: a + b)(1, 2))

# 내장 함수에서 자주 사용되는 람다 함수
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b: a + b, list1, list2)
print(list(result))
