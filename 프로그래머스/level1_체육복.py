def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                answer += 1
                lost[i] -= 100
                reserve[j] -= 200
                break
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if abs(lost[i] - reserve[j]) == 1:
                answer += 1
                reserve[j] -= 200
                break
    return answer