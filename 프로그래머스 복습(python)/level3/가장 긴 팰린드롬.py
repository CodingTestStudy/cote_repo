def check_odd(start, s):
    cnt = 0
    step = 1
    while start - step >= 0 and start + step < len(s):
        if s[start - step] == s[start + step]:
            cnt += 1
            step += 1
        else:
            break

    return cnt


def check_even(left, right, s):
    cnt = 0
    step = 0
    while left - step >= 0 and right + step < len(s):
        if s[left - step] == s[right + step]:
            cnt += 1
            step += 1
        else:
            break
    return cnt


def solution(s):
    answer_odd = -1
    answer_even = -1
    for i in range(len(s)):
        answer_odd = max(answer_odd, check_odd(i, s))
        answer_even = max(answer_even, check_even(i, i + 1, s))
    answer = max(answer_odd * 2 + 1, answer_even * 2)
    return answer


print(solution("abcdcba"))  # 7
print(solution("abacde"))  # 3
