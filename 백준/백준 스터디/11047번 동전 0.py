import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 동전 종류 개수, 가치의 합 입력
coin = []   # 동전의 종류를 저장할 리스트
idx = 0
for i in range(n): # n번의 반복문을 통해
    x = int(input()) # 동전을 입력받고
    coin.append(x) # 동전 리스트에 저장
    if x < k: # 만약 입력받은 동전의 값이 K원보다 커지기 전까지
        idx = i # idx값을 갱신, 결국엔 idx는 K원보다 작은 동전 중 가장 큰 값의 index를 저장
        # 문제의 입력 예시의 경우
        # K = 4200, idx = 1000의 index

count = 0
for i in range(idx, -1, -1): # K보다 작은 동전에 대해서만 반복
    count += k // coin[i] # K에서 해당 동전값을 나눈 값들을 count에 축적
    k %= coin[i] # K값을 해당 동전 값과 나눈 나머지값으로 갱신
    if k == 0: # K값이 0이 될때까지 반복 후, 반복문 종료
        break

print(count) # 해당 count값 출력


