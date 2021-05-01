def solution(arr):
    if len(arr) == 1:
        return [-1]

    min_index = 0
    for i in range(1, len(arr)):
        min_value = arr[min_index]
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
    del arr[min_index]
    return arr

arr = [4, 3, 2, 1]
print(solution(arr))

# 삭제 연산이 없으므로 더 효율적인 코드
# def sol(arr):
#     min_value = min(arr)
#     return [i for i in arr if i > min_value] or [-1]
