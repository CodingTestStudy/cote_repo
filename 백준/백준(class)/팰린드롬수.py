result = []
while True:
    data = input()
    if data == "0":
        break

    length = len(data) // 2
    array1 = []
    array2 = []
    for i in range(length):
        array1.append(data[i])
    for j in range(len(data) - 1, len(data) - length - 1, -1):
        array2.append(data[j])
    if array1 == array2:
        result.append("yes")
    else:
        result.append("no")

for i in range(len(result)):
    print(result[i])
