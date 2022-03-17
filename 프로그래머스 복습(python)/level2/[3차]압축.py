def solution(msg):
    answer = []
    alpha_dict = dict()
    for i in range(1, 27):
        alpha_dict[chr(i + 64)] = i

    start = 0
    while start != len(msg):
        end = len(msg)
        while True:
            # dict에서 일치하는 가장 긴 key 문자 찾기(end값을 줄여가면서 일치하는 문자 찾기)
            temp = msg[start:end]
            if temp in alpha_dict.keys():
                answer.append(alpha_dict[temp])
                break
            end -= 1
        # dict에 새로운 문자에 추가
        alpha_dict[msg[start:end + 1]] = len(alpha_dict) + 1
        # 출발지점 갱신, K -> A -> KA( "K -> A (X)" ) -> O
        start = end
    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
