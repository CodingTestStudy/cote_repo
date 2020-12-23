import datetime

# 2020년 12월 23일을 표현
d_day = datetime.datetime(2020, 1, 16)
print(d_day)

# 2020년 12월 23일 15시 50분 10초를 표현
d_day = datetime.datetime(2020, 1, 16, 11, 20, 30)
print(d_day)

# 오늘 날짜와 현재 시간을 표현
today = datetime.datetime.now()
print(today)

# 위에서 설정한 시간과 현재 시간 사이의 기간을 표현
# 기존의 뺄셈 연산과 동일하게 계산한다.
print(today - d_day)


# datetime 값에서 각 요소들만 추출
today = datetime.datetime.now()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)