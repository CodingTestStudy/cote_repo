import sys

# input method
# input() : 함수의 한 줄의 문자열을 입력 받는 함수
# map() : 리스트의 모든 원소에 각각 특정한 함수를 적용

# ex) 공백을 기준으로 구분된 데이터를 입력 받을 때
# list(map(int, input().split()))

# ex) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면
# a, b, c = map(int , input().split()))

# 데이터 개수 입력
n = int(input("데이터 개수 : "))
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input("공백 구분하여 입력 : ").split()))

print("기존 리스트")
print(data)
print("내림차순")
data.sort(reverse=True)
print(data)

# 빠르게 입력받기
# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우
# 입력 후 엔터가 줄 바꿈 기호로 입력됙 떄문에 rstrip() 메서드 함께 사용
data = sys.stdin.readline().rstrip()
print(data)


# print()에서 줄바꿈을 원치 않을 떄
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")
print("a, b의 합은 " + str(a+b) + "입니다.")


