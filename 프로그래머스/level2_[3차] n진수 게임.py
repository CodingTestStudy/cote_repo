def solution(n, t, m, p):
    n_list = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
        6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
        11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    num = "01"

    # 접근할 가능성이 있는 가장 최대값까지 해당 진수로 만들고
    for i in range(2, m*t + 1):
        num_list = []
        while i > n - 1:
            num_list.append(n_list[i % n])
            i //= n
        num_list.append(n_list[i])

        # 문자열로 이어붙임
        while num_list:
            num += num_list.pop()

    # 본인 순서에 필요한 값들만 골라서 문자열로 저장
    answer = ''
    for i in range(t):
        answer += num[m*i + p-1]
    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))