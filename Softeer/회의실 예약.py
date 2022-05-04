from collections import defaultdict

N, M = map(int, input().split())
name = []
for _ in range(N):
    name.append(input().strip())
name.sort()

room = defaultdict(list)
for _ in range(M):
    r, s, t = input().split()
    start, end = int(s), int(t)
    room[r].append([start, end])

for n in name:
    room[n].sort()


def make_time(time):
    if time < 10:
        return '0' + str(time)
    return str(time)


def calc(temp):
    result = []
    start = 9
    for s, e in temp:
        if s > start:
            result.append(make_time(start) + '-' + make_time(s))
        start = e
    if start != 18:
        result.append(make_time(start) + '-' + '18')

    return result


for idx, n in enumerate(name):
    print(f"Room {n}:")
    result = calc(room[n])
    if not result:
        print("Not available")
    else:
        print(f"{len(result)} available:")
        for data in result:
            print(data)

    if idx != len(name) - 1:
        print("-----")
