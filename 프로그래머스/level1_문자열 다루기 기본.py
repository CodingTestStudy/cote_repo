def length(s):
    if len(s) == 4 or len(s) == 6:
        return True
    return False

def only_num(s):
    for value in s:
        if not(48 <= ord(value) <= 57):
            return False
    return True

def solution(s):
    if length(s) and only_num(s):
        return True
    return False

print(solution("1234"))

# sol 1
# return s.isdigit() and len(s) in (4, 6)

# sol 2
#     try:
#         int(s)
#     except:
#         return False
#     return len(s) == 4 or len(s) == 6