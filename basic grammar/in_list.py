
# value 값이 list 안에 존재하는지 확인하는 함수
def check_value(c_list, value):
    i = 0
    while i < len(c_list):
        # list 안에서 value 값과 동일한 값이 존재하면 True return
        if c_list[i] == value:
            return True
        i += 1

    # list 안에 value 값과 동일한 값이 존재하지 않는다면 False return
    return False


# 함수를 구현한 방법
some_list = [1, 2, 3, 4, 5]
print(some_list, 1)
print(some_list, 10)


# 간단한 방법
some_list = [1, 2, 3, 4, 5]
print(1 in some_list)
print(10 in some_list)
print(1 not in some_list)
print(10 not in some_list)


