S = input()
result = [] # 문자열의 그룹을 나눠서 저장하기 위한 리스트
data = '' # 문자를 구분짓기 위해 사용할 임의의 문자 저장 변수

def reverse(S): # 문자열 뒤집는 함수
    s = list(S)
    length = len(s) - 1
    for k in range(length // 2 + 1):
        s[k], s[length - k] = s[length - k], s[k]
    return s


for i in range(len(S)): # 문자열 내의 문자 하나하나에 대해서
    if len(data) > 0 and data[0] == '<': # 기존에 문자가 < 로 시작한다면
        data += S[i] # 기존 문자에 현재 문자 추가
        if S[i] == '>': # 현재 문자가 > 라면
            result.append(data) # 결과 리스트에 삽입하고
            data = '' # 기존 문자 초기화
    elif len(data) > 0 and S[i] == '<': # 기존 문자가 존재하고, 현재 문자가 < 라면
        result.append(data) # 기존에 존재하던 문자를 결과 리스트에 삽입하고
        data = '<' # 기존 문자를 < 로 처음부터 시작
    elif S[i] == ' ': # 현재 문자가 공백이라면
        result.append(' ' + data) # 기존 문자 앞에 공백을 추가해서 결과 리스트에 삽입, 괄호 없이 끝나는 문자를 위해
        data = '' # 기존 문자 초기화
    else:
        data += S[i] # 그외의 일반적인 경우, 기본 문자에 현재 문자 추가
        if i == len(S) - 1: # 현재 문자가 마지막 문자라면
            result.append(data) # 기존 문자 결과 리스트에 삽입


for i in range(len(result)):
    if result[i][0] != '<': # 결과 리스트 중에서, <> 안에 존재하지 않는 문자의 경우
        result[i] = ''.join(reverse(result[i])) # 뒤집어서 저장

for value in result: # 결과 리스트에 있는 데이터
    print(value, end='') # 출력
print()
