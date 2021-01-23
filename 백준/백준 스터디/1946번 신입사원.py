# from collections import deque
import sys
import heapq
T = int(input())    # 테스트 케이스 개수 (1 <= T <= 20)
grade = [[] for _ in range(T)]
for i in range(T):
    N = int(sys.stdin.readline())   # 신입사원  수(1 <= N <= 100,000)
    for _ in range(N):
        document, interview = map(int, sys.stdin.readline().split())
        heapq.heappush(grade[i], (document, interview))

# 서류 순위로 정렬한 후, 인터뷰 순위를 비교함
# 반복문을 통해 서류순위가 내려가면서
# 본인의 서류순위가 높은 신입사원 중에서, 인터뷰 순위도 높은 신입사원이 존재한다면
# 전체 신입사원 인원에서 배제
for i in range(T):
    q = []  # 본인보다 서류순위가 높은 신입사원중에서 가장 높은 인터뷰 순위를 구하기 위한 리스트(힙 사용)
    pick = len(grade[i])    # i번째 테스트케이스의 신입사원 인원 수
    temp_d, temp_i = heapq.heappop(grade[i])
    heapq.heappush(q, temp_i)   # 아래의 반복문을 위해, 임의로 먼저 q에 삽입
    while grade[i]:
        behind_d, behind_i = heapq.heappop(grade[i])    # 비교대상이 될 순위들
        x = heapq.heappop(q)    # 비교 대상보다 높은 서류 순위 중, 가장 높은 인터뷰 순위
        if x < behind_i:    # 본인이 서류순위도 낮은데, 인터뷰 순위도 낮은 경우
            pick -= 1  # 4 < 5
        heapq.heappush(q, x)    # 높은 인터뷰 순위 다시 삽입
        heapq.heappush(q, behind_i) # 본인의 인터뷰 순위도 삽입
    print(pick)

