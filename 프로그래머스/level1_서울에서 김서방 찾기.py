def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = "김서방은 " + str(i) + "에 있다"
    return answer

print(solution(["Jane", "Kim"]))

# return "김서방은 {}에 있다".format(seoul.index('Kim'))