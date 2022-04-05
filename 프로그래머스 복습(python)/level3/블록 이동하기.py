from collections import deque


def next_location_list(loc, board):
    temp = []
    (r1, c1), (r2, c2) = loc
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 상하좌우 이동
    for i in range(4):
        nr1, nc1 = r1 + dr[i], c1 + dc[i]
        nr2, nc2 = r2 + dr[i], c2 + dc[i]
        # 범위 확인
        if nr1 < 0 or nr1 >= len(board) or nc1 < 0 or nc1 >= len(board):
            continue
        if nr2 < 0 or nr2 >= len(board) or nc2 < 0 or nc2 >= len(board):
            continue

        if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
            temp.append({(nr1, nc1), (nr2, nc2)})

    # 세로 -> 가로
    if c1 == c2:
        for i in [-1, 1]:
            if 0 <= c1 + i < len(board) and 0 <= c2 + i < len(board):
                if board[r1][c1 + i] == 0 and board[r2][c2 + i] == 0:
                    temp.append({(r1, c1), (r1, c1 + i)})
                    temp.append({(r2, c2), (r2, c2 + i)})
    elif r1 == r2:
        for i in [-1, 1]:
            if 0 <= r1 + i < len(board) and 0 <= r2 + i < len(board):
                if board[r1 + i][c1] == 0 and board[r2 + i][c2] == 0:
                    temp.append({(r1, c1), (r1 + i, c1)})
                    temp.append({(r2, c2), (r2 + i, c2)})

    # (r1, c1), (r2, c2) 에서 이동할 수 있는 좌표 리스트 반환
    return temp


def solution(board):
    n = len(board) - 1

    # 현재 위치 + 가중치
    q = deque()
    now = {(0, 0), (0, 1)}
    q.append((now, 0))
    location = [now]
    while q:
        loc, cost = q.popleft()

        # 현재 위치 중, 도착 위치가 존재하면 종료
        if (n, n) in loc:
            return cost

        # 현재 위치에서 이동 가능한 좌표들
        for nxt in next_location_list(loc, board):
            # 이동 가능 좌표(가로, 세로 따로)가 이전에 방문한적 없다면
            if nxt not in location:
                # 방문처리
                location.append(nxt)
                # 다음 위치 + 가중치 증가
                q.append((nxt, cost + 1))


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
