from string import ascii_uppercase, ascii_lowercase
from collections import deque
def solution(str1, str2):
    str1 = deque(str1)
    str2 = deque(str2)
    alphabet = ascii_lowercase + ascii_uppercase
    A, B = [], []
    while len(str1) != 1:
        s = str1[0] + str1[1]
        if not(str1[0] not in alphabet or str1[1] not in alphabet):
            A.append(s.upper())
        str1.popleft()
    while len(str2) != 1:
        s = str2[0] + str2[1]
        if not (str2[0] not in alphabet or str2[1] not in alphabet):
            B.append(s.upper())
        str2.popleft()

    # 둘다 공집합일 경우
    if not A and not B:
        return 65536

    intersection, union = [], []
    for value in A:
        c1 = min(A.count(value), B.count(value))
        c2 = max(A.count(value), B.count(value))
        if value not in intersection:
            for _ in range(c1):
                intersection.append(value)
        if value not in union:
            for _ in range(c2):
                union.append(value)
    for value in A:
        if value not in union:
            for _ in range(A.count(value)):
                union.append(value)
    for value in B:
        if value not in union:
            for _ in range(B.count(value)):
                union.append(value)

    if not intersection and not union:
        return 65536

    return int(len(intersection) / len(union) * 65536)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
