# 효율성을 위해 이중 연결 리스트 사용
def solution(n, k, cmd):
    linked_list = dict()
    for i in range(n):
        linked_list[i] = [i - 1, i + 1]
    deleted = ["O" for _ in range(n)]
    deleted_list = []

    now = k
    for command in cmd:
        # 아래 이동
        if command[0] == "D":
            step = int(command[2:])
            for _ in range(step):
                now = linked_list[now][1]
        # 위 이동
        elif command[0] == "U":
            step = int(command[2:])
            for _ in range(step):
                now = linked_list[now][0]
        # 삭제
        elif command[0] == "C":
            prev, nxt = linked_list[now]
            deleted_list.append([prev, now, nxt])
            deleted[now] = "X"

            # 삭제 대상 다음이 존재하지 않는다면(즉 현재 마지막 행이면), 위 행으로 위치 이동
            if nxt == n:
                now = linked_list[now][0]
            else:
                now = linked_list[now][1]

            # 삭제 처리 후, 삭제 대상 위, 아래 연결 작업
            # 삭제 대상이 맨 위라면, 다음이 맨 위로 연결
            if prev == -1:
                linked_list[nxt][0] = prev
            # 삭제 대상이 맨 아래라면, 바로 위가 맨 아래로 연결
            elif nxt == n:
                linked_list[prev][1] = nxt
            # 삭제 대상이 가운데라면 위아래 연결
            else:
                linked_list[prev][1] = nxt
                linked_list[nxt][0] = prev
        # 복구
        else:
            prev, _now, nxt = deleted_list.pop()
            deleted[_now] = "O"

            if prev == -1:
                linked_list[nxt][0] = _now
            elif nxt == n:
                linked_list[prev][1] = _now
            else:
                linked_list[prev][1] = _now
                linked_list[nxt][0] = _now
    return "".join(deleted)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))

# # 효율성 오답
# def solution(n, k, cmd):
#     status = ["O"] * n
#     deleted_list = []
#     now = k
#     for command in cmd:
#         # 행 삭제
#         if command[0] == "C":
#             # 삭제 대상이 마지막 행인지 확인
#             last_live_r = n - 1
#             for i in range(n - 1, -1, -1):
#                 if status[i] == "O":
#                     last_live_r = i
#                     break
#             # 삭제 처리
#             status[now] = "X"
#             deleted_list.append(now)
#
#             # 삭제 대상이 마지막 행인지에 따라 위, 아래로 이동
#             nxt = -1 if now == last_live_r else 1
#             while status[now] == "X":
#                 now = (now + nxt) % n
#
#         # 최근 삭제 행 복구
#         elif command[0] == "Z":
#             restore_idx = deleted_list.pop()
#             status[restore_idx] = "O"
#
#         # 행 이동
#         else:
#             order, step = command.split(" ")[0], int(command.split(" ")[1])
#             cnt = 0
#             nxt = 1 if order == "D" else -1
#             while cnt != step:
#                 now = (now + nxt) % n
#                 if status[now] == "X":
#                     continue
#                 cnt += 1
#     return "".join(status)
