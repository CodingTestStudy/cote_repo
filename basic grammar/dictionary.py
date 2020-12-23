# 사전 자료형, c의 struct나 java의 hashmap과 비슷

# 사전 자료형 선언1
fruits = dict()
fruits['사과'] = 'Apple'
fruits['바나나'] = 'Banana'
fruits['코코넛'] = 'Coconut'

print(fruits)

if '사과' in fruits:
    print("'사과' 존재함")

# key 값만 추출
key = fruits.keys()
# value 값만 추출
value = fruits.values()
print("fruits key 값들 : ", list(key))
print("fruits value 값들 :", list(value))

# 사전 자료형 선언2
color = {
    '빨강': 'red',
    '파랑': 'blue',
    '노랑': 'yellow'
}

print(color)

if '빨강' in color:
    print("'빨강' 존재함")

# 각 key에 대한 value값들 하나씩 출력
for i in color:
    print(color[i])
