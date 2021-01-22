N = int(input())
data = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

max_result = -int(1e9)
min_result = int(1e9)

def rotation(index, result):
    global max_result, min_result
    if index == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if op[0] > 0:
        op[0] -= 1
        rotation(index + 1, result + data[index])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        rotation(index + 1, result - data[index])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        rotation(index + 1, result * data[index])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        rotation(index + 1, int(result/data[index]))
        op[3] += 1


rotation(1, data[0])
print(max_result)
print(min_result)