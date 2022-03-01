def solution(participant, completion):
    participant.sort()
    completion.sort()

    while participant:
        if participant[-1] == completion[-1]:
            participant.pop()
            completion.pop()
        else:
            break
    return participant.pop()


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["eden", "kiki"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))