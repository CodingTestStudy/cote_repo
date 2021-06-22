def solution(dirs):
    answer = 0
    visited = [(0, 0, 0, 0)]
    move = dict(zip(["U", "D", "L", "R"], [0, 1, 2, 3]))

    # 상하좌우
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    for value in dirs:
        now = visited[-1]
        nr = now[2] + dr[move[value]]
        nc = now[3] + dc[move[value]]
        # 범위 조건 만족하면
        if -5 <= nr <= 5 and -5 <= nc <= 5:
            if (now[2], now[3], nr, nc) not in visited:
                answer += 1
            visited.append((nr, nc, now[2], now[3]))
            visited.append((now[2], now[3], nr, nc))
    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))

# another solution 집합사용
def another_solution(dirs):
    s = set()
    d = {"U":(0, 1), "D":(0, -1), "R":(1, 0), "L":(-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    return len(s)//2

print(another_solution("ULURRDLLU"))
print(another_solution("LULLLLLLU"))