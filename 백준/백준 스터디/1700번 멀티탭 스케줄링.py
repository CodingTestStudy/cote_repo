import sys
N, K = map(int, sys.stdin.readline().strip().split())
item = list(map(int, sys.stdin.readline().strip().split()))

plug = [0] * N
swap = 0
count = 0
max_index = 0
for i in range(len(item)):
    if item[i] in plug: pass # 해당 기기가 플러그에 꽂혀있는 경우
    elif 0 in plug: plug[plug.index(0)] = item[i] # 플러그가 비어있는 경우, 해당 기기 꽂는다.
    else:
        for value in plug:
            if value not in item[i:]:
                swap = value
                break
            elif item[i:].index(value) > max_index:
                max_index = item[i:].index(value)
                swap = value
        plug[plug.index(swap)] = item[i]
        max_index = 0
        swap = 0
        count += 1
print(count)
