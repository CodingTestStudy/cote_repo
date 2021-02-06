import heapq
import sys
N = int(input())
data = []
for _ in range(N):
    data.append((list(map(int, sys.stdin.readline().rstrip().split()))))

# 시작 시간을 기준으로 오름차순 정렬
data.sort()
# 강의가 끝나는 시간들을 저장, 끝나는 시간이 다른 강의들의 개수를 통해
# 강의실 개수가 최소 몇개 필요한지 구함
q = []

for s, t in data:
    heapq.heappush(q, t)
    if q[0] <= s:
        heapq.heappop(q)
        # 반복문을 통해 각 케이스의 시작 시간이
        # 이전에 출적된 끝나는 시간들 중 가장 작은 시간과
        # 같거나 크면, 해당 강의실에서 강의 시작
        # 끝난 강의는 heappop()으로 빠져나감
        # 즉, 강의 끝나는 시간과 강의 시작시간끼리 꼬리를 무는 경우,
        # 위에서 heappsuh()와 아래의 heappop()을 통해 바통터치 느낌

# 결국에는 다른 강의와 switch되지 못하고 남아있는 강의들이
# 남은 강의실 개수
result = len(q)
print(result)