def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()

    print(new_id)
    # 2단계
    for value in new_id:
        if value.isalpha() or value.isdigit() or value in ['-', '_', '.']:
            answer += value
    print(answer)
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    print(answer)
    # 4단계
    if len(answer) >= 1 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) >= 1 and answer[-1] == '.':
        answer = answer[:-1]

    print(answer)
    # 5단계
    if len(answer) == 0:
        answer = 'a'

    print(answer)
    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    print(answer)
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]

    return answer

print(solution("=.="))