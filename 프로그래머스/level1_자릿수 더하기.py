def solution(n):
    answer = 0
    s = str(n)
    for i in s:
        answer += int(i)

    return answer

print(solution(987))

# return sum(map(int, str(number)))
# return sum([int(i) for i in str(number)])