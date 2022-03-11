def solution(sizes):
    max_wight = 0
    max_height = 0
    for size in sizes:
        size.sort()
        max_wight = max(max_wight, size[0])
        max_height = max(max_height, size[1])
    return max_wight * max_height
    # return max(max(x) for x in sizes) * max(min(x) for x in sizes)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
