T = int(input())
for idx in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    last = num_list[-1]
    answer = 0
    for i in range(N - 1, -1, -1):
        if last > num_list[i]:
            answer += last - num_list[i]
        else:
            last = num_list[i]

    print(f"#{idx} {answer}")
