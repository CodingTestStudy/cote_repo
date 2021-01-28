S = input()
result = 0
temp = 1
flag = False
q = []
for i in range(len(S)):
    if S[i] == '(':
        temp *= 2
        q.append('(')
    elif S[i] == '[':
        temp *= 3
        q.append('[')
    elif S[i] == ')':
        if len(q) == 0 or q[len(q) - 1] != '(':
            flag = True
            break
        else:
            if S[i - 1] == '(':
                result += temp
            q.pop()
            temp //= 2
    elif S[i] == ']':
        if len(q) == 0 or q[len(q) - 1] != '[':
            flag = True
            break
        else:
            if S[i - 1] == '[':
                result += temp
            q.pop()
            temp //= 3

if flag or len(q) != 0:
    print(0)
else:
    print(result)