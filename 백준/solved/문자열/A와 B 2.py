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
    return del_a(word[:-1]) or del_b(word[:-1])


def del_b(word):
    if not word:
        return False
    if word == S:
        return True
    if word[0] != 'B':
        return False
    word.reverse()
    return del_a(word[:-1]) or del_b(word[:-1])


if del_a(T) or del_b(T):
    print(1)
else:
    print(0)
