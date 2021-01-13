# 채점 결과
# 정확성: 42.9
# 효율성: 7.1
# 합계: 50.0 / 100.0
def solution(food_times, k):
    answer = 0
    INF = int(1e8) + 1
    routine = len(food_times)
    while True:
        min_value = min(food_times)
        x = min_value * routine
        if k >= x:
            k -= x
            for i in range(len(food_times)):
                if food_times[i] != INF:
                    food_times[i] -= min_value
                    
                    if food_times[i] == 0:
                        routine -= 1
                        food_times[i] = INF
        elif k >= routine:
            y = k // routine
            k -= routine * y
            for i in range(len(food_times)):
                if food_times[i] != INF:
                    food_times[i] -= y
                    if food_times[i] == 0:
                        routine -=1
                        food_times[i] = INF
        else:
            break
    while True:
        for i in range(len(food_times)):
            if food_times[i] == INF:
                continue
            else:
                food_times[i] -= 1
                k -= 1
                if k == -1:
                    answer = i + 1
                    return answer
                            
print(solution([3, 1, 2], 5))