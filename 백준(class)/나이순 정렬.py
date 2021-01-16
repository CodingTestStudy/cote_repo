n = int(input())
name_list = [[] for _ in range(201)]
for _ in range(n):
    age, name = input().split()
    name_list[int(age)].append(name)
for i in range(201):
    if name_list[i] != "":
        for j in name_list[i]:
            print(i, j)
