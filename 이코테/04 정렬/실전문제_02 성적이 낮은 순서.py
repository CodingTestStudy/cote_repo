n = int(input())
student = []
for i in range(n):
  student.append(list(input().split()))

def setting(data):
  return data[1]

student = sorted(student, key=setting)

for i in student:
  print(i[0], end=' ')
