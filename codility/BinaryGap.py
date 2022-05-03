def solution(N):
    data = bin(N)[2:]

    start = 0
    gap = 0
    for i in range(1, len(data)):
        if data[i] == '1':
            gap = max(gap, i - start - 1)
            start = i
    return gap
