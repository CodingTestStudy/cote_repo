def solution(prices):
    answer = []
    for i in range(len(prices)):
        step = 0
        target = prices[i]
        for j in range(i + 1, len(prices)):
            step += 1
            if target > prices[j]:
                break
        answer.append(step)
    return answer


print(solution([1, 2, 3, 2, 3]))

def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        for j in range(i + 1, len(prices)):
            time += 1
            if prices[i] > prices[j]:
                break
        answer.append(time)

    return answer