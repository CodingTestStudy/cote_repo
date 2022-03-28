def possible(frame):
    for x, y, kind in frame:
        # 기둥
        if kind == 0:
            # 바닥인 경우
            if y == 0:
                continue
            # 양쪽에 보가 존재하거나, 밑에 기둥이 존재하는 경우
            elif (x - 1, y, 1) in frame or (x, y, 1) in frame or (x, y - 1, 0) in frame:
                continue
            else:
                return False
        # 보
        else:
            # 양쪽에 기둥이 존재하거나, 양쪽에 보가 존재하는 경우
            if (x, y - 1, 0) in frame or (x + 1, y - 1, 0) in frame or (
                    (x - 1, y, 1) in frame and (x + 1, y, 1) in frame):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    # [r, c, a, b]
    # a -> 0: 기둥, 1: 보
    # b -> 0: 삭제, 1: 설치
    answer = []
    for x, y, a, b in build_frame:
        # 삭제
        if b == 0:
            if (x, y, a) in answer:
                answer.remove((x, y, a))
                if not possible(answer):
                    answer.append((x, y, a))
        # 설치
        else:
            answer.append((x, y, a))
            if not possible(answer):
                answer.remove((x, y, a))

    return sorted(answer)


print(solution(5,
               [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                [3, 2, 1, 1]]))
print(solution(5,
               [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                [2, 0, 0, 0],
                [1, 1, 1, 0], [2, 2, 0, 1]]))
