n = int(input())
student = []
for _ in range(n):
    #student.append(list(input().split()))
    input_data = input().split()
    student.append((input_data[0], int(input_data[1])))

data = sorted(student, key=lambda x : x[1])
for value in data:
    print(value[0], end=' ')
