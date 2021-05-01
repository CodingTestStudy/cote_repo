def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        x = ""
        x1 = bin(arr1[i])[2:]
        x2 = bin(arr2[i])[2:]

        if len(x1) != n:
            x1 = (n - len(x1)) * '0' + x1
        if len(x2) != n:
            x2 = (n - len(x2)) * '0' + x2

        for j in range(len(x1)):
            if int(x1[j]) == 0 and int(x2[j]) == 0:
                x += ' '
            else:
                x += '#'
        answer.append(x)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))

# rjust : 오른쪽 정렬
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer