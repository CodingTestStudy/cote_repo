def solution(n):
    n_list = []
    while n != 0:
        n_list.append(n % 10)
        n //= 10
    return n_list

print(solution(12345))

# return list(map(int, reversed(str(n))))
# return [int(i) for i in str(n)][::-1]