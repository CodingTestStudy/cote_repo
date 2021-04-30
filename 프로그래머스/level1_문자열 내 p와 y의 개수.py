def solution(s):
    answer = True
    p = 0 # 80, 112
    y = 0 # 89, 121
    for value in s:
        if ord(value) == 80 or ord(value) == 112:
            p += 1
        elif ord(value) == 89 or ord(value) == 121:
            y += 1

    if p == 0 and y == 0:
        return True
    if p - y == 0:
        return True
    else:
        return False

print(solution("Pyy"))

# return s.lower().count('p') == s.lower().count('y')