# 무지의 먹방 라이브
def solution(food_times, k):
    while True:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                continue
            else:
                food_times[i] -= 1
                k -= 1
                print(food_times)
                if k == -1:
                  return i + 1        

print(solution([3, 1, 2], 5))