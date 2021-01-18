n, m = map(int, input().split())
array = list(map(int, input().split()))
sum_list = []
array.sort()
for i in range(len(array) - 2):
    for j in range(i + 1, len(array) - 1):
        for k in range(j + 1, len(array)):
            sum = array[i] + array[j] + array[k]
            if sum <= m:
                sum_list.append(sum)


print(max(sum_list))



