import sys
sys.setrecursionlimit(10000) # 재귀 횟수 조정
N = int(sys.stdin.readline().strip())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
blue = 0
white = 0

def rotation(a, b, n):
    global blue, white # 전역변수 사용하기 위해 선언
    p = data[a][b] # 일치되어야하는 대상(첫 번째 값), 첫 번째 값과 다르면 의미없음
    flag = True # p와 일치하는지 여부 판단
    for i in range(a, a + n):
        if not flag:
            break
        for j in range(b, b + n):
            if p != data[i][j]:
                flag = False # p와 일치하지 않으면, 다시 분할 및 재귀
                n //= 2 # 분할을 위해 길이 반으로 나누고
                # 4등분 분할한 값들을 각 함수에 삽입(재귀)
                rotation(a, b, n)
                rotation(a, b + n, n)
                rotation(a + n, b, n)
                rotation(a + n, b + n, n)
                break

    if flag: # a, b 범위 내의 데이터들이 모두 p와 일치하다면
        if p: # p값이 1이라면
            blue += 1 # 파랑색 추가
        else: # p값이 0이라면
            white += 1 # 흰색 추가


rotation(0, 0, N)
print(white)
print(blue)
