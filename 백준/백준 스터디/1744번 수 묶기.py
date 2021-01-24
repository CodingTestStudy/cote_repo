import heapq
n = int(input())
plus = []   # 0보다 큰 값들을 저장할 리스트
minus = []  # 0이하의 값들을 저장할 리스트
for _ in range(n):  # n번 만큼
    data = int(input()) # 정수를 입력받고
    # 해당 값의 조건에 맞는 각각 리스트에 삽입
    if data > 0: heapq.heappush(plus, -data) # 최대 힙
    else: heapq.heappush(minus, data) # 최소 힙

sum = 0
while plus: # plus 리스트가 빌 때까지
    temp1 = -heapq.heappop(plus) # 현재 plus 리스트에서의 가장 큰 값
    if not plus: # 이제 plus 리스트가 비어있다면
        sum += temp1 # 덧셈으로 마무리
        break
    temp2 = -heapq.heappop(plus) # 현재 plus 리스트에서의 가장 큰 값
    if temp2 == 1: sum += temp1 + temp2 # 만약 두 번째 값이 1이라면, 덧셈(곱셈하는 것보다 덧셈이 더 큰값을 만듬)
    else: sum += temp1 * temp2 # 둘다 1보다 크다면 곱셈 (덧셈보다 곱셈이 더 큰값을 만듬)

while minus: # minus 리스트가 빌 때까지
    temp1 = heapq.heappop(minus) # 현재 minus 리스트에서의 가장 작은 값
    if not minus: # 이제 minus 리스트가 비어있다면
        sum += temp1 # 뺄셈으로 마무리 (temp1는 어차피 음수이기 때문에 += 사용)
        break
    temp2 = heapq.heappop(minus) # 현재 minus 리스트에서의 가장 작은 값
    sum += temp1 * temp2 # (음수, 음수) or (음수, 0)의 경우, 곱셈의 결과가 가장 큰 값을 만듬

print(sum)


