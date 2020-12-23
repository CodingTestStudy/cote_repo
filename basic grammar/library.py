from itertools import permutations, combinations, product, combinations_with_replacement
from collections import Counter
import math

# 실전에서 유용한 표준 라이브러리

# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능을 제공
# -> 특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용됨

# heapq : 힙(Heap) 자료구조를 제공
# -> 일반적으로 우선순위 큐 기능을 구현하기 위해 사용

# bisect : 이진 탐색(Binary Search) 기능을 제공

# collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조 포힘

# math : 필수적인 수학적 기능 제공
# -> 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수 , 파이 등등 포함


# sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(1, 2, 3, 4, 5)
max_result = max(1, 2, 3, 4, 5)
print("min : ", min_result)
print("max : ", max_result)

# eval
result = eval("(3+5)*7")
print(result)

# 순열
# from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# 조합
# from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

# 중복 순열
# from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))  # 2개 뽑는 모든 순열 구하기 (중복 허용)
print(result)

# 중복 조합
# from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))  # 2개 뽑는 모든 조합 구하기 (중복 허용)
print(result)


# Counter : 등장 횟수를 세는 기능
# from collections import Counter

counter = Counter(['rad', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])  # 'blue' 등장 횟수
print(counter['green']) # 'green' 등장 횟수
print(dict(counter))    # 사전 자료형으로 형변환


# 최대 공약수 -> math 라이브러리의 gcd() 함수 사용
# import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(x, y):
    # a 와 b의 곱과 최대공약수의 몫을 리턴
    return x * y // math.gcd(x, y)


a = 21
b = 14

print("a, b의 최대공약수 : ", math.gcd(a, b))
print("a, b의 최소공배수 : ", lcm(a, b))
