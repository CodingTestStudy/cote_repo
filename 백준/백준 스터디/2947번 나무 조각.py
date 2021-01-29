data = list(map(int, input().split()))

def print_data(): # 현재 리스트 출력하는 함수
    for x in range(5):
        print(data[x], end=' ')
    print()

while not (data[0] == 1 and data[1] == 2 and data[2] == 3 and data[3] == 4 and data[4] == 5):
    for i in range(4): # 1, 2, 3, 4단계를 위한 반복문
        if data[i] > data[i + 1]: # 각 단계의 조건에 만족한다면
            data[i], data[i + 1] = data[i + 1], data[i] # 데이터 값 변경
            print_data() # 변경 후의 리스트 출력
