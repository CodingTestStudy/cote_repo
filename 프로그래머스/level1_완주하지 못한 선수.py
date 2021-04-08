def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    while completion:
        if participant[-1] == completion[-1]:
            participant.pop()
            completion.pop()
        else:
            break
    return participant.pop()