def solution(a, b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    # 1월 1일이 금요일이므로, 7로 나눴을 때 인덱스 1이 금요일로 나오게 배열 설정
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # mon배열의 (a-1)월까지 더한 수에
    return day[(sum(mon[:a-1]) + b) % 7]

print(solution(5, 24))