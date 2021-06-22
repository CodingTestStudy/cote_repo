def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        s_list = []
        for j in range(len(arr2[0])):
            data = 0
            for k in range(len(arr1[0])):
                data += arr1[i][k] * arr2[k][j]
            s_list.append(data)
        answer.append(s_list)

    return answer

 # answer = [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
 #    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))