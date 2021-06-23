def solution(s):
    num_list = s.split(" ")
    num_list = list(map(int, num_list))
    num_list.sort()
    return str(num_list[0]) + " " + str(num_list[-1])

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))

# another solution
def solution(s):
    s = list(map(int, s.split()))
    return str(min(s)) + " " + str(max(s))

