from collections import defaultdict, deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(start, end, board, visited, target):
    n = len(board)
    q = deque([(start, end)])
    ret = {(0, 0)}
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 범위 이탈
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if board[nr][nc] == target and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))

                # [0, 0] 위치를 기준
                ret.add((nr - start, nc - end))
    return ret


def rotate(board, n):
    result = set()
    for r, c in board:
        result.add((c, n - r - 1))
    return result


def find_block(block, set_block, n):
    for _ in range(4):
        mr, mc = min(block)
        new_block = set()
        for r, c in block:
            new_block.add((r - mr, c - mc))
        if new_block in set_block:
            set_block.remove(new_block)
            return len(new_block)

        block = rotate(block, n)
    return 0


def solution(game, table):
    answer = 0
    num_of_block = defaultdict(list)
    n = len(table)

    visited = [[False] * n for _ in range(n)]
    # 블럭 개수별로 블럭의 위치 저장
    for r in range(n):
        for c in range(n):
            if table[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                block = bfs(r, c, table, visited, 1)
                num_of_block[len(block)].append(block)
    # 빈 공간 찾기
    visited = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if game[r][c] == 0 and not visited[r][c]:
                visited[r][c] = True
                empty_block = bfs(r, c, game, visited, 0)
                if len(empty_block) in num_of_block:
                    answer += find_block(empty_block, num_of_block[len(empty_block)], n)

    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))
