import sys
N = int(sys.stdin.readline().strip())
crane = sorted(list(map(int, sys.stdin.readline().strip().split())), reverse=True)
M = int(sys.stdin.readline().strip())
box = sorted(list(map(int, sys.stdin.readline().strip().split())), reverse=True)

visited = [0 for _ in range(M)]
position = [0] * N
count = 0
time = 0

if box[0] > crane[0]: print(-1)
else:
    while count < len(box):
        for i in range(N):
            while position[i] < len(box):
                if not visited[position[i]] and crane[i] >= box[position[i]]:
                    # print("***")
                    # print(position[i])
                    # print(box[position[i]])
                    # print(crane[i])
                    visited[position[i]] = True
                    position[i] += 1
                    count += 1
                    # print("position = ", position)
                    # print("***")
                    break
                position[i] += 1
                # print(i, "번쩨 position 증가", position)
        time += 1

    print(time)
