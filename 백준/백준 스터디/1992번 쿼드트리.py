import sys
N = int(input())
data = [sys.stdin.readline().rstrip() for _ in range(N)]

def rotation(x1, y1, x2, y2, n):
    if n == 1: return data[y1][x1] # 분할 결과 결국 하나만 남게 된다면, 그 자체 return
    a = n // 2 # 현재 길이에서 2등분

    # 4등분으로 분할
    r1 = rotation(x1, y1, x1 + a, y1 + a, a)
    r2 = rotation(x1 + a, y1, x1 + n, y1 + a, a)
    r3 = rotation(x1, y1 + a, x1 + a, y1 + n, a)
    r4 = rotation(x1 + a, y1 + a, x1 + n, y1 + n, a)

    # 모두 같은 값일 경우 하나만 출력
    if r1 == r2 == r3 == r4 and len(r1) == 1: return r1 # 분할되어 보인 값들이 모두 같다면, 하나만 return
    return "(" + r1 + r2 + r3 + r4 + ")"

print(rotation(0, 0, N, N, N))

