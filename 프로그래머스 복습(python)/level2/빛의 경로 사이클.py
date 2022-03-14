def calculate(r, c, i, visited, grid):
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    nr, nc, index = r, c, i
    step = 0
    visited[r][c][i] = True
    while True:
        nr = (nr + dr[index]) % len(grid)
        nc = (nc + dc[index]) % len(grid[0])
        step += 1

        if grid[nr][nc] == 'R':
            index = (index + 1) % 4
        elif grid[nr][nc] == 'L':
            index = (index - 1) % 4
        if visited[nr][nc][index]:
            if (r, c, i) == (nr, nc, index):
                return step
            else:
                return 0
        visited[nr][nc][index] = True


def solution(grid):
    visited = [[[False] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    answer = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for i in range(4):
                if not visited[r][c][i]:
                    step = calculate(r, c, i, visited, grid)
                    if step != 0:
                        answer.append(step)
    answer.sort()
    return answer


print(solution(["SL", "LR"]))
print(solution(["S"]))
print(solution(["R", "R"]))
