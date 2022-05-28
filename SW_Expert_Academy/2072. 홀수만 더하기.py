T = int(input())
for i in range(1, T + 1):
    data = list(map(int, input().split()))
    answer = 0
    for num in data:
        if num % 2 == 1:
            answer += num
    print(f"#{i} {answer}")
