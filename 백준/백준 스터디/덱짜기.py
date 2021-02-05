A, B, K = map(int, input().split())
if A < 3 or B < 2: print(0)
else:
    deq_count = 0 # 만든 덱의 개수
    remain = 0 # 잉여 카드 개수
    A3_count = A // 3 # A를 3개로 묶은 개수
    A -= A3_count * 3 # A 남은 개수
    B2_count = B // 2 # B를 2개로 묶은 개수
    B -= B2_count * 2 # B 남은 개수

    if A3_count > B2_count:
        A += (A3_count - B2_count) * 3
        deq_count = B2_count
    else:
        B += (B2_count - A3_count) * 2
        deq_count = A3_count

    remain = A + B
    if K <= remain:
        print(deq_count)
    else:
        K -= remain
        K //= 5
        K += 1
        print(deq_count - K)

