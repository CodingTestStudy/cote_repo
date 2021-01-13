# 럭키 스트레이트 (10 <= n <= 99,999,999)
n = input()
m = []
result = 0
for value in n:
    m.append(int(value))

for i in range(len(m)):
    if i < len(m) // 2:
        result += m[i]
    else:
        result -= m[i]

if result == 0:
    print("LUCKEY")
else:
    print("READY")
