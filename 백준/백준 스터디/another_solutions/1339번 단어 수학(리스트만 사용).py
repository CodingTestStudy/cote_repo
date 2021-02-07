# 리스트만 사용
N = int(input())
sum_list = [0 for _ in range(26)]   # 26개의 알파벳 리스트

for _ in range(N):  # 입력된 문자열 횟수만큼 반복
    temp = input()  # 문자열 입력
    for i in range(len(temp)):  # 문자열내의 모든 문자에 대해서
        sum_list[ord(temp[i]) - 65] += 10 ** (len(temp) - i - 1)
sum_list.sort(reverse=True)
idx = 0
result = 0
for i in range(9, 0, -1):
    result += sum_list[idx] * i
    idx += 1
print(result)
