# 무지의 먹방 라이브
def solution(food_times, k):
    answer = 0   
    repeat = len(food_times)
    x = True
    while x:
      for i in range(0, repeat):
        if k == -1: 
          x = False
          break
        if food_times[i] == 0: continue
        else:
          food_times[i] -= 1
          k -= 1
          answer = i + 1                         
    
    return answer


# f = list(map(int, input().split()))
# k = int(input())
# print(solution(f, k))

# 입력 3 1 2
# 입력 5
# 결과 1

# 입력 8 6 4
# 입력 15
# 결과 2
