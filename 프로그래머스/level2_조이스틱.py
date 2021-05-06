def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0

        # name 을 완성한 경우
        if sum(make_name) == 0: break

        left, right = 1, 1

        # 현재위치(idx)를 기준으로 양방향으로 아직 안다룬 알파벳 탐색
        while make_name[idx - left] == 0: left += 1
        while make_name[idx + right] == 0: right += 1

        # 가까운 방향으로 누적값과 위치 갱신
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer

print(solution("JAZ"))
print(solution("JEROEN"))
print(solution("JAN"))
