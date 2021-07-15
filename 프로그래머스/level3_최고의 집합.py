def solution(n, s):
    # 더한 값들이 s가 될 수 없는 경우
    if n > s:
        return [-1]

    x = s // n
    # s가 n개로 나눠 떨어진 경우
    if n * x == s:
        return [x] * n

    # s가 n개로 나눠 떨어지지 않는 경우
    else:
        y = s % n
        answer = [x] * n
        length = len(answer) - 1

        # x값에 나머지를 고르게 분배
        while y != 0:
            answer[length] += 1
            y -= 1
            length -= 1
        return answer

print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))