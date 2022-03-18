def solution(citations):
    answer = []
    h = 1
    while h < max(citations):
        up, down = 0, 0
        for c in citations:
            if c >= h:
                up += 1
            else:
                down += 1
        if up >= h >= down:
            answer.append(h)
        h += 1
    if not answer:
        return 0
    return max(answer)


print(solution([3, 0, 6, 1, 5]))


# better code
# def solution(citations):
#     citations.sort()
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l - i:
#             return l - i
#     return 0
