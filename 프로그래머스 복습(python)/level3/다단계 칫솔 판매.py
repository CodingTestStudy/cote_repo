from collections import defaultdict, deque


def solution(enroll, referral, seller, amount):
    name_dict = dict()
    price_dict = defaultdict(list)

    for i in range(len(referral)):
        if referral[i] == "-":
            name_dict[enroll[i]] = "center"
            continue
        name_dict[enroll[i]] = referral[i]

    for i in range(len(seller)):
        q = deque([[seller[i], amount[i] * 100]])
        while q:
            my_name, my_price = q.popleft()
            if my_price // 10 < 1:
                price_dict[my_name].append(my_price)
                break
            else:
                your_price = my_price // 10
                my_price -= your_price
                price_dict[my_name].append(my_price)
                if name_dict[my_name] == "center":
                    price_dict[name_dict[my_name]].append(your_price)
                    break
                q.append([name_dict[my_name], your_price])

    return [sum(price_dict[name]) for name in enroll]


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))
