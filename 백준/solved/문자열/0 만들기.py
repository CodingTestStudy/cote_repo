import sys
from copy import deepcopy

input = sys.stdin.readline
T = int(input())


def make_op(temp, cnt):
    if cnt == N - 1:
        op_list.append(deepcopy(temp))
        return
    temp.append(' ')
    make_op(temp, cnt + 1)
    temp.pop()

    temp.append('+')
    make_op(temp, cnt + 1)
    temp.pop()

    temp.append('-')
    make_op(temp, cnt + 1)
    temp.pop()


while T:
    T -= 1
    N = int(input())
    op_list = []
    make_op([], 0)

    nums = [i for i in range(1, N + 1)]

    for op in op_list:
        test = ''
        for i in range(N - 1):
            test += str(nums[i]) + op[i]
        test += str(N)

        if eval(test.replace(' ', '')) == 0:
            print(test)
    print()
