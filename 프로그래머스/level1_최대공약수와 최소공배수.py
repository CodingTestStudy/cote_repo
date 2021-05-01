def gcd(n, m):
    if n < m:
        n, m = m, n
    r = n % m

    while r != 0:
        n = m
        m = r
        r = n % m
    return m

def lcm(n, m, g):
    return n * m // g

def solution(n, m):
    g = gcd(n, m)
    return [g, lcm(n, m, g)]

print(solution(2, 5))