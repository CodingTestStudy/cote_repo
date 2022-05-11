data = list(input().strip())
bomb = list(input().strip())

temp = []
for c in data:
    temp.append(c)
    # temp의 마지막 문자가 폭발 마지막 문자와 일치하고,
    # 폭발 문자 길이보다 긴 경우(폭발 문자가 있는지 검사해도 되는 경우)
    if temp[-1] == bomb[-1] and len(temp) >= len(bomb):
        # 해당 위치에 폭발 문자가 존재하면
        if temp[-len(bomb):] == bomb:
            # 폭발 문자 길이만큼 pop
            for _ in range(len(bomb)):
                temp.pop()

if temp:
    print("".join(temp))
else:
    print("FRULA")
