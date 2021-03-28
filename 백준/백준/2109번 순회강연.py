import sys
N = int(input())
# 0 <= N <= 10000 이므로 N == 0인 경우 따로 분류
if N == 0: print(0)
else:
    lecture = []
    for i in range(N):
        p, d = map(int, sys.stdin.readline().strip().split())
        lecture.append((d, p))
    lecture.sort()
    last_day = lecture[-1][0] # deadline 제일 늦은 날
    q = [] # 강연할 대학 후보 저장 리스트
    result = 0 # 최종 pay
    for i in range(last_day, 0, -1): # deadline 이 가장 늦은 날부터 강연 지정
        while lecture and lecture[-1][0] >= i: # i일보다 dealine이 긴 강연이면
            q.append(lecture.pop()[1]) # 해당 강연의 pay를 저장
        if q: # 강연 후보가 존재한다면
            q.sort()
            result += q.pop() # 가장 큰 pay 지정(pay 누적)
    print(result)
