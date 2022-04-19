from itertools import combinations

n = int(input())
number_list = []
for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        # 숫자 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)
        number_list.append(int(''.join(map(str, comb))))
number_list.sort()

if n < len(number_list):
    print(number_list[n])
else:
    print(-1)
