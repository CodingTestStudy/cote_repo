def solution(n, k, cmd):
    status = ["O"] * n
    deleted_list = []
    now = k
    for command in cmd:
        # 행 삭제
        if command[0] == "C":
            # 삭제 대상이 마지막 행인지 확인
            last_live_r = n - 1
            for i in range(n - 1, -1, -1):
                if status[i] == "O":
                    last_live_r = i
                    break
            # 삭제 처리
            status[now] = "X"
            deleted_list.append(now)

            # 삭제 대상이 마지막 행인지에 따라 위, 아래로 이동
            nxt = -1 if now == last_live_r else 1
            while status[now] == "X":
                now = (now + nxt) % n

        # 최근 삭제 행 복구
        elif command[0] == "Z":
            restore_idx = deleted_list.pop()
            status[restore_idx] = "O"

        # 행 이동
        else:
            order, step = command.split(" ")[0], int(command.split(" ")[1])
            cnt = 0
            nxt = 1 if order == "D" else -1
            while cnt != step:
                now = (now + nxt) % n
                if status[now] == "X":
                    continue
                cnt += 1
    return "".join(status)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
