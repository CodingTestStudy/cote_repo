def quadTree(arr, answer, x, y, length):
    total = calculate(arr, x, y, length)
    # 1칸인 경우
    if length == 1:
        answer[arr[x][y]] += 1
    # 1칸보다 많은 상태에서 압축되는 경우
    elif total == 0 or total == length * length:
        if total == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    # 다시 나눠줘야 하는 경우
    else:
        length //= 2
        quadTree(arr, answer, x, y, length)
        quadTree(arr, answer, x + length, y, length)
        quadTree(arr, answer, x, y + length, length)
        quadTree(arr, answer, x + length, y + length, length)


def calculate(arr, x, y, length):
    total = 0
    for i in range(x, x + length):
        for j in range(y, y + length):
            total += arr[i][j]
    return total


def solution(arr):
    if arr.count(1) == len(arr) * len(arr):
        return [0, arr.count(1)]
    elif arr.count(1) == len(arr) * len(arr):
        return [arr.count(1), 0]
    else:
        answer = [0, 0]
        quadTree(arr, answer, 0, 0, len(arr))
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))