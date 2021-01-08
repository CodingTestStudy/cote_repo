import sys

# 데이터의 개수입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

print()

n, m, k = map(int, input().split())
print(n, m, k)


# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)

answer = 7
print("정답은 " + str(answer) + "입니다.")

answer = 7
print("정답은", str(answer), "입니다.")

answer = 7
print(f"정답은 {answer}입니다.")


