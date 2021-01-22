import sys
N = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
operator = list(map(int, input().split()))  # +, -, *, //
plus = operator[0]
minus = operator[1]
multiply = operator[2]
divide = operator[3]
temp_op = []

count = 0
while count != N - 1:
    if multiply != 0:
        temp_op.append('*')
        multiply -= 1
    elif plus != 0:
        temp_op.append('+')
        plus -= 1
    elif divide != 0:
        temp_op.append('//')
        divide -= 1
    else:
        temp_op.append('-')
        minus -= 1
    count += 1

temp = data
for i in range(N - 1):
    x = temp_op.pop()
    if x == '*': temp[i + 1] = temp[i] * temp[i + 1]
    elif x == '+': temp[i + 1] = temp[i] + temp[i + 1]
    elif x == '//': temp[i + 1] = temp[i] // temp[i + 1]
    else: temp[i + 1] = temp[i] - temp[i + 1]

print(temp[N - 1])
