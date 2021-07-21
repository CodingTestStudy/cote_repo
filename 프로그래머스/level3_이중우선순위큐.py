import heapq

# 참고
# heapq.nlargest(n, q) q에서 가장 큰 순으로 n개를 뺀다.
# heapq.nsmallest(n, q) q에서 가장 작은 순으로 n개를 뺀다.

def solution(operations):
    min_q = []
    max_q = []

    for i in range(len(operations)):
        command = operations[i].split()

        # 숫자 삽입
        if command[0] == 'I':
            num = int(command[1])
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)

        else:
            # 삭제할 데이터가 없다면
            if not min_q:
                pass

            # 최댓값 삭제
            elif int(command[1]) == 1:
                max_value = -heapq.heappop(max_q)
                min_q.remove(max_value)

            # 최솟값 삭제
            else:
                min_value = heapq.heappop(min_q)
                max_q.remove(-min_value)

    if not min_q:
        return [0, 0]
    return [-heapq.heappop(max_q), heapq.heappop(min_q)]


print(solution(["I 16", "D 1"]))
print((solution(["I 7", "I 5", "I -5", "D -1"])))
print(solution(["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]))
