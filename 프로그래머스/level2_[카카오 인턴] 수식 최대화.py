from itertools import permutations

def isinteger(s):
    return s.isdigit() or s[0] == '-' and s[1:].isdigit()

def solution(expression):
    op = []
    if '-' in expression:
        op.append('-')
    if '+' in expression:
        op.append('+')
    if '*'in expression:
        op.append('*')

    word = ""
    exp_list = []
    for i in range(len(expression)):
        if expression[i].isdigit():
            word += expression[i]
        else:
            exp_list.append(word)
            exp_list.append(expression[i])
            word = ""
        if i == len(expression) - 1:
            exp_list.append(word)

    priority_op = list(permutations(op))

    result = 0
    for i in range(len(priority_op)):
        temp = exp_list[:]
        last = 0
        for j in range(len(priority_op[i])):
            for k in range(len(temp)):
                if temp[k] == priority_op[i][j]:
                    left, right = k, k
                    while not isinteger(temp[left]):
                        left -= 1
                    while not isinteger(temp[right]):
                        right += 1

                    temp[k] = str(eval(temp[left] + temp[k] + temp[right]))

                    temp[left], temp[right] = '@', '@'
                    last = k
        result = max(abs(int(temp[last])), result)
    return result


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
print(solution("2-990-5+2"))
print(solution("2*2*2*2*2-2*2*2"))