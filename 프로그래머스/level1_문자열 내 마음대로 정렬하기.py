def solution(strings, n):
    temp = []
    answer = []
    strings.sort()

    for i in range(len(strings)):
        temp.append((strings[i][n], i))
    temp.sort(reverse=True)

    while temp:
        answer.append(strings[temp.pop()[1]])
    return answer

strings = ["abce", "abcd", "cdx"]
n = 2
solution(strings, n)


# return sorted(sorted(strings), key=lambda x: x[n])
# return sorted(strings, key = lambda x : x[n]+x[:])