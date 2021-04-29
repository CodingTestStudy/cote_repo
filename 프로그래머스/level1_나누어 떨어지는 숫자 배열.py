def solution(arr, divisor):
    answer = []
    for value in arr:
        if value % divisor == 0:
            answer.append(value)

    if not answer:
        answer.append(-1)

    answer.sort()

    return answer

arr = [3, 2, 6]
divisor = 10
print(solution(arr, divisor))

# def solution(arr, divisor):
#     arr = [x for x in arr if x % divisor == 0];
#     arr.sort();
#     return arr if len(arr) != 0 else [-1];