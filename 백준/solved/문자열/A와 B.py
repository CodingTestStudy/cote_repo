import sys

sys.setrecursionlimit(10 ** 6)
S = list(input())
T = list(input())


def del_a(word):
    if not word:
        return False
    if word == S:
        return True
    if word[-1] != 'A':
        return False
    word.pop()
    return del_a(word) or del_b(word)


def del_b(word):
    if not word:
        return False
    if word == S:
        return True
    if word[-1] != 'B':
        return False
    word.pop()
    word.reverse()
    return del_a(word) or del_b(word)


if del_a(T) or del_b(T):
    print(1)
else:
    print(0)
