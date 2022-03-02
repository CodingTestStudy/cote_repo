def solution(clothes):
    clothes_dict = {}
    for name, type in clothes:
        if type not in clothes_dict.keys():
            clothes_dict[type] = 1
        else:
            clothes_dict[type] += 1
    answer = 1
    for value in clothes_dict.values():
        # 각 type의 의상 중 아무것도 안입는 경우도 다루기 때문에 +1
        answer *= (value + 1)

    #아무것도 안입은 경우 제외
    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))