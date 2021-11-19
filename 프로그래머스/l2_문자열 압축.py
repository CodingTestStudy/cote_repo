def solution(s):
    answer = []
    result = ""

    # 한글자만 있으면 1 반환
    if len(s) == 1:
        return 1

    # 1부터 문자열 절바 길이까지 단위 잘라서 확인
    for cut in range(1, len(s) // 2 + 1):
        count = 1
        temp = s[:cut]

        for i in range(cut, len(s), cut):
            if s[i:i + cut] == temp:
                count += 1
            else:
                if count == 1:
                    count = ""

                result += str(count) + temp
                temp = s[i:i + cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + temp
        answer.append(len(result))
        result = ""
    return min(answer)

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))