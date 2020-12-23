name = "규림"
age = 25
# 가장 오래된 방식
print("제 이름은 %s이고 %d살 입니다." % (name, age))
# 현재 가장 많이 쓰는 방식 (format 메소드)
print("제 이름은 {}이고 {}살 입니다.".format(name, age))
# 새로운 방식 (f-string) -> 파이썬 버전 3.6부터
print(f"제 이름은 {name}이고 {age}살 입니다.")
