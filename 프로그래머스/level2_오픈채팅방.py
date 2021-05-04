def solution(record):
    d = {}
    answer = []
    for i in record:
        if i[0] == 'E' or i[0] == 'C':
            d[i.split(" ")[1]] = i.split(" ")[2]

    for i in record:
        if i[0] == 'E':
            answer.append(d[i.split(" ")[1]] + "님이 들어왔습니다.")
        elif i[0] == 'L':
            answer.append(d[i.split(" ")[1]] + "님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]))
