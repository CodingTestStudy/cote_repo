def solution(line):
    answer = []
    top, bottom, left, right = -1e13, 1e13, 1e13, -1e13
    line_intersect = set()
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            if a * d - b * c != 0:
                x = (b * f - e * d) / (a * d - b * c)
                y = (e * c - a * f) / (a * d - b * c)
                if x % 1 == 0 and y % 1 == 0:
                    line_intersect.add((int(x), int(y)))
                    top = max(top, int(y))
                    bottom = min(bottom, int(y))
                    left = min(left, int(x))
                    right = max(right, int(x))
    for y in range(top, bottom - 1, -1):
        ans = ""
        for x in range(left, right + 1):
            if (x, y) in line_intersect:
                ans += "*"
            else:
                ans += "."
        answer.append(ans)
    return answer


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
