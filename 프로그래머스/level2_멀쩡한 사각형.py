import math

def solution(w,h):
    g = math.gcd(w, h)
    return w * h - (w + h - g)

print(solution(8, 12))