from collections import deque

def solution(dartResult):
    dart = deque(dartResult)
    answer = []
    num = ""
    num_digit = 0
    while dart:
        x = dart.popleft()

        # 숫자일 경우
        if x.isdigit():
           num += x

        # 숫자가 아닌 경우
        elif x in ["S", "D", "T"]:
            num_digit = int(num)
            num = ""
            if x == "D":
                num_digit **= 2
            elif x == "T":
                num_digit **= 3

           # 옵션인 경우
            if dart and dart[0] == "*":
                dart.popleft()
                num_digit *= 2
                if answer:
                    answer[-1] *= 2
            elif dart and dart[0] == "#":
                dart.popleft()
                num_digit *= -1

            answer.append(num_digit)
    return sum(answer)

print(solution("1D2S#10S"))