# 못 푼 문제

def solution(s):
    answer = []
    result = ""

    # 한글자 밖에 없으면 1 반환
    if len(s) == 1:
        return 1

    # 1~문자열 절반 길이까지 cut 단위로 잘라서 확인해봄
    for cut in range(1, len(s) // 2 + 1):
        count = 1
        temp = s[:cut] # 비교해볼 문자열 단위
        for i in range(cut, len(s), cut):
            # 해당 범위의 문자열이 비교해볼 문자열 단위와 동일하다면
            if s[i:i+cut] == temp:
                count += 1 # 반복된 문자열 횟수 증가
            else:
                # 이전까지 반복된 적이 없다면 문자열 앞에 아무것도 안붙임
                if count == 1:
                    count = ""
                result += str(count) + temp # temp 의 반복된 횟수를 문자열로 붙임
                temp = s[i:i+cut] # 새로운 문자열 단위 갱신
                count = 1 # 다시 count 시작
        if count == 1:
            count = ""
        result += str(count) + temp # 남아있는 문자열 더하기
        answer.append(len(result)) # cut 단위로 압축해본 결과의 길이 저장
        result = ""

    return min(answer)

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))