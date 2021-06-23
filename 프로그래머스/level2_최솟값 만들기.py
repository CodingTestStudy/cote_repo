def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    return sum(a * b for a, b in zip(A, B))

print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))